from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from . import utils, storage, decision_engine
import uuid, os

router = APIRouter()

@router.post('/verify')
async def verify(id_file: UploadFile = File(...), selfie_file: UploadFile = File(...)):
    token = str(uuid.uuid4())
    tmpdir = '/tmp/kyc'
    os.makedirs(tmpdir, exist_ok=True)
    id_path = os.path.join(tmpdir, f'{token}_id.jpg')
    selfie_path = os.path.join(tmpdir, f'{token}_selfie.jpg')

    with open(id_path, 'wb') as f:
        f.write(await id_file.read())
    with open(selfie_path, 'wb') as f:
        f.write(await selfie_file.read())

    q = utils.check_image_quality(id_path)
    if not q['ok']:
        return JSONResponse({'status':'error','message': q['message']})

    extracted = utils.perform_ocr(id_path)
    face = utils.compare_faces(selfie_path, id_path)
    decision = decision_engine.compute_decision(extracted, face)

    audit_root = os.path.join(os.path.dirname(__file__), 'audit')
    os.makedirs(audit_root, exist_ok=True)
    storage.save_audit(audit_root, token, id_path, selfie_path, extracted, face, decision)

    resp = {
        'token': token,
        'decision': decision,
        'extracted': {'lines': extracted.get('lines', [])[:10]},
        'face': face
    }
    return JSONResponse(resp)
