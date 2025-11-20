from PIL import Image, ImageStat
import pytesseract
import cv2
import numpy as np
import os

def check_image_quality(path):
    try:
        im = Image.open(path)
        stat = ImageStat.Stat(im.convert('L'))
        bright = stat.mean[0]
        if bright < 18:
            return {'ok': False, 'message': 'Image too dark'}
        if im.size[0] < 300 or im.size[1] < 200:
            return {'ok': False, 'message': 'Image resolution too low'}
        return {'ok': True}
    except Exception as e:
        return {'ok': False, 'message': f'Quality check failed {str(e)}'}

def perform_ocr(path):
    try:
        img = Image.open(path)
        text = pytesseract.image_to_string(img)
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        return {'raw_text': text, 'lines': lines}
    except Exception as e:
        return {'raw_text': '', 'lines': [], 'error': str(e)}

def _detect_face_cv2(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    haar_xml = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(haar_xml)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30,30))
    return faces

def compare_faces(selfie_path, id_path):
    try:
        img1 = cv2.imdecode(np.fromfile(selfie_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        img2 = cv2.imdecode(np.fromfile(id_path, dtype=np.uint8), cv2.IMREAD_COLOR)
        if img1 is None or img2 is None:
            return {'match': False, 'reason': 'Could not read images'}

        f1 = _detect_face_cv2(img1)
        f2 = _detect_face_cv2(img2)
        if len(f1) == 0 or len(f2) == 0:
            return {'match': False, 'reason': 'No face detected in one of images'}

        x,y,w,h = f1[0]
        crop1 = img1[y:y+h, x:x+w]
        x2,y2,w2,h2 = f2[0]
        crop2 = img2[y2:y2+h2, x2:x2+w2]

        crop1 = cv2.resize(crop1, (200,200))
        crop2 = cv2.resize(crop2, (200,200))

        orb = cv2.ORB_create(500)
        kp1, des1 = orb.detectAndCompute(cv2.cvtColor(crop1, cv2.COLOR_BGR2GRAY), None)
        kp2, des2 = orb.detectAndCompute(cv2.cvtColor(crop2, cv2.COLOR_BGR2GRAY), None)
        if des1 is None or des2 is None:
            return {'match': False, 'reason': 'Could not compute descriptors'}

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(des1, des2)
        if not matches:
            return {'match': False, 'distance': 1.0, 'reason': 'No descriptor matches'}

        distances = [m.distance for m in matches]
        avg_dist = sum(distances) / len(distances)
        sim = max(0.0, 1.0 - (avg_dist / 300.0))
        match = sim > 0.35
        return {'match': bool(match), 'similarity': float(sim), 'avg_distance': float(avg_dist)}
    except Exception as e:
        return {'match': False, 'reason': str(e)}
