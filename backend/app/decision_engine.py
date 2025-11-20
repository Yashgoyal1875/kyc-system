import os
import joblib
import numpy as np

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'sample_risk_model.pkl')
try:
    model = joblib.load(MODEL_PATH)
except Exception:
    model = None

def compute_decision(extracted, face):
    reasons = []
    face_score = 1.0 if face.get('match') else 0.0
    lines = len(extracted.get('lines', []))
    device_rep = 0.5

    if model is not None:
        x = np.array([[1 if face_score>0.5 else 0, lines, device_rep]])
        try:
            prob = float(model.predict_proba(x)[0,1])
        except Exception:
            prob = face_score * 0.6 + min(1.0, lines / 5.0) * 0.4
    else:
        prob = face_score * 0.6 + min(1.0, lines / 5.0) * 0.4

    score = round(prob * 100, 2)
    if score >= 70:
        status = 'approved'
    elif score >= 45:
        status = 'needs_review'
    else:
        status = 'rejected'

    if not face.get('match'):
        reasons.append('face_mismatch')
    if lines < 2:
        reasons.append('insufficient_ocr')

    return {'status': status, 'score': score, 'reasons': reasons}
