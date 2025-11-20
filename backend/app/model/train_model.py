# backend\app\model\train_model.py
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
import joblib, os

X = []
y = []
for i in range(400):
    face = 1 if i % 2 == 0 else 0
    lines = (i % 5) + 1
    device = np.random.rand()
    X.append([face, lines, device])
    label = 1 if face == 1 and lines >= 2 and device > 0.2 else 0
    y.append(label)

clf = GradientBoostingClassifier()
clf.fit(X, y)
joblib.dump(clf, 'sample_risk_model.pkl')
print('model saved at', os.path.abspath('sample_risk_model.pkl'))
