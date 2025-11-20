import os, json, shutil
from datetime import datetime

def save_audit(audit_root, token, id_path, selfie_path, extracted, face, decision):
    dest = os.path.join(audit_root, token)
    os.makedirs(dest, exist_ok=True)
    shutil.copy(id_path, os.path.join(dest, 'id.jpg'))
    shutil.copy(selfie_path, os.path.join(dest, 'selfie.jpg'))
    with open(os.path.join(dest, 'extracted.json'), 'w') as f:
        json.dump(extracted, f, indent=2)
    with open(os.path.join(dest, 'face.json'), 'w') as f:
        json.dump(face, f, indent=2)
    with open(os.path.join(dest, 'decision.json'), 'w') as f:
        json.dump(decision, f, indent=2)
    with open(os.path.join(dest, 'meta.json'), 'w') as f:
        json.dump({'token': token, 'ts': datetime.utcnow().isoformat()}, f, indent=2)
