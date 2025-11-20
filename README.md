🚀 Seamless Trust Engine – KYC Verification System

"Instant Identity. Zero Friction."

FastAPI Backend • React Frontend • OCR & Face Matching • Audit Tracking • Docker Compose

🎯 Overview

This project is a complete end to end KYC (Know Your Customer) verification engine designed for identity onboarding flows.

It performs:

📸 ID document & selfie capture

🔍 OCR text extraction

🧠 Face similarity matching

🎯 Risk scoring

🗂️ Full audit storage

🌐 Containerized frontend & backend

Ideal for hackathons, demos, fintech prototypes, and security validation use-cases.

🌟 Why this KYC System?

✔️ Works fully offline — no external APIs
✔️ Face embedding + similarity model
✔️ OCR extraction with full audit trail
✔️ Modern React capture UI
✔️ Saves all decisions for compliance
✔️ Docker based deployment

🚀 Quick Start (Docker)
1️⃣ Build & Start
docker compose up --build

2️⃣ Open Frontend
http://localhost:5173

3️⃣ View Backend API Docs
http://localhost:8000/docs

🧩 Features
Feature	Description
📸 Document + Selfie Capture	React webcam flows
🔍 OCR	Extract ID text via Tesseract
🧠 Face Match	OpenCV + face recognition embeddings
🎯 Scoring Model	Simple risk engine
📁 Audit Folders	Stores id.jpg, selfie.jpg, decision.json
🔄 Reproducible	Every verification stored by token
🔧 Local Dev Friendly	Zero cloud dependencies
📦 Docker Included	Simple deployment
🏗️ Architecture
               ┌────────────────────────────┐
               │        React Frontend       │
               │   Webcam capture flow       │
               └───────────────┬────────────┘
                               │
                          POST /api/verify
                               ▼
                   ┌─────────────────────────┐
                   │      FastAPI Backend     │
                   │ 1. Save Files            │
                   │ 2. OCR Extraction        │
                   │ 3. Face Match            │
                   │ 4. Risk Engine           │
                   │ 5. Audit Logging         │
                   └──────────────┬──────────┘
                                  ▼
                   ┌─────────────────────────┐
                   │      Audit Storage       │
                   │  token/                  │
                   │    id.jpg                │
                   │    selfie.jpg            │
                   │    decision.json         │
                   │    extracted.json        │
                   │    face.json             │
                   └─────────────────────────┘

🔄 Verification Workflow
1 — Capture

User captures ID image + selfie.

2 — Backend Processing

Saves images

OCR on ID

Face comparison

Decision scoring

3 — Audit Logging

Each attempt gets a unique token with full JSON metadata.

4 — Response Returned

Frontend receives:

decision

similarity score

extracted text

token folder

📁 Project Structure
kyc-system/
│
├── backend/
│   ├── app/
│   │   ├── api.py
│   │   ├── main.py
│   │   ├── decision_engine.py
│   │   ├── storage.py
│   │   ├── utils.py
│   │   └── model/
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── Style.css
│   ├── dockerfile
│   └── package.json
│
├── docker-compose.yml
└── README.md

🧪 API Reference
POST /api/verify
Form data:

id_file — ID document image

selfie_file — selfie image

Example response:
{
  "token": "2559e1f2-c50a-4049-9bc1-948bdbc5ecee",
  "decision": { "status": "accepted", "score": 0.82 },
  "face": { "match": true, "similarity": 0.84 },
  "extracted": { "lines": ["NAME", "COUNTRY", "ID 12345678"] }
}

🐛 Troubleshooting
Issue	Fix
Backend unreachable	Confirm backend on port 8000
CORS in console	Ensure frontend fetch URL = http://localhost:8000
OCR returns empty text	Improve lighting / zoom ID properly
Face mismatch	Use clear, frontal selfie
Docker constantly fails	Run docker compose down -v then rebuild
🛣️ Roadmap

 Multi document types

 Better OCR parsing (fields extraction)

 Machine learning based fraud detection

 Live anti spoofing

 Cloud ready deployment module

📄 License

MIT License.
