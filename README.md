# 🚀 Seamless Trust Engine – KYC Verification System

<div align="center">

![KYC Banner](https://img.shields.io/badge/KYC-Verification%20Engine-0078D4?style=for-the-badge&logo=shield-check&logoColor=white)

**"Instant Identity. Zero Friction."**

[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-61DAFB?style=flat&logo=react&logoColor=black)](https://reactjs.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Features](#-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [API Docs](#-api-reference) • [Roadmap](#️-roadmap)

</div>

---

## 🎯 Overview

A **complete end-to-end KYC (Know Your Customer) verification engine** designed for seamless identity onboarding flows. Built for hackathons, demos, fintech prototypes, and security validation use-cases.

### What It Does

- 📸 **ID Document & Selfie Capture** — Real-time webcam integration
- 🔍 **OCR Text Extraction** — Automated document parsing with Tesseract
- 🧠 **Face Similarity Matching** — AI-powered face recognition
- 🎯 **Risk Scoring Engine** — Intelligent decision making
- 🗂️ **Full Audit Storage** — Compliance-ready logging
- 🐳 **Containerized Deployment** — One-command setup with Docker

---

## 🌟 Why Choose This KYC System?

<table>
<tr>
<td>

✅ **100% Offline Capable**  
No external APIs required

</td>
<td>

✅ **AI-Powered Matching**  
Face embeddings + similarity scoring

</td>
</tr>
<tr>
<td>

✅ **Complete Audit Trail**  
Every verification logged & traceable

</td>
<td>

✅ **Modern React UI**  
Intuitive capture flow

</td>
</tr>
<tr>
<td>

✅ **Compliance Ready**  
Stores all decisions for regulatory needs

</td>
<td>

✅ **Docker Deployment**  
Production-ready containerization

</td>
</tr>
</table>

---

## 🚀 Quick Start

### Prerequisites

- **Docker** & **Docker Compose**
- (Optional) **Node.js 18+** and **Python 3.9+** for local development

### One-Command Setup

```bash
# Clone the repository
git clone https://github.com/Yashgoyal1875/kyc-system.git
cd kyc-system

# Build and start all services
docker compose up --build
```

### Access the Application

| Service | URL | Description |
|---------|-----|-------------|
| 🎨 **Frontend** | [http://localhost:5173](http://localhost:5173) | React UI for KYC capture |
| ⚡ **Backend API** | [http://localhost:8000](http://localhost:8000) | FastAPI service |
| 📚 **API Docs** | [http://localhost:8000/docs](http://localhost:8000/docs) | Interactive Swagger UI |

---

## 🧩 Features

<table>
<thead>
<tr>
<th>Feature</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr>
<td>📸 <strong>Document + Selfie Capture</strong></td>
<td>Seamless webcam integration with React for real-time image capture</td>
</tr>
<tr>
<td>🔍 <strong>OCR Extraction</strong></td>
<td>Powered by Tesseract to extract text from ID documents</td>
</tr>
<tr>
<td>🧠 <strong>Face Matching</strong></td>
<td>OpenCV + face_recognition library for embedding-based comparison</td>
</tr>
<tr>
<td>🎯 <strong>Scoring Model</strong></td>
<td>Simple but effective risk engine for decision making</td>
</tr>
<tr>
<td>📁 <strong>Audit Folders</strong></td>
<td>Stores <code>id.jpg</code>, <code>selfie.jpg</code>, <code>decision.json</code> per verification</td>
</tr>
<tr>
<td>🔄 <strong>Reproducible</strong></td>
<td>Every verification stored with unique token for traceability</td>
</tr>
<tr>
<td>🔧 <strong>Local Dev Friendly</strong></td>
<td>Zero cloud dependencies — runs entirely offline</td>
</tr>
<tr>
<td>📦 <strong>Docker Included</strong></td>
<td>Simple, consistent deployment across environments</td>
</tr>
</tbody>
</table>

---

## 🏗️ Architecture

```
                ┌────────────────────────────┐
                │      React Frontend        │
                │   Webcam capture flow      │
                │   (Port 5173)              │
                └───────────────┬────────────┘
                                │
                           POST /api/verify
                                │
                                ▼
                    ┌─────────────────────────┐
                    │    FastAPI Backend      │
                    │    (Port 8000)          │
                    │                         │
                    │  1. Save Files          │
                    │  2. OCR Extraction      │
                    │  3. Face Match          │
                    │  4. Risk Engine         │
                    │  5. Audit Logging       │
                    └──────────────┬──────────┘
                                   ▼
                    ┌─────────────────────────┐
                    │    Audit Storage        │
                    │    ./audits/            │
                    │      ├── token/         │
                    │      │   ├── id.jpg     │
                    │      │   ├── selfie.jpg │
                    │      │   ├── decision.json│
                    │      │   ├── extracted.json│
                    │      │   └── face.json  │
                    └─────────────────────────┘
```

---

## 🔄 Verification Workflow

### Step 1: Capture 📸
User captures ID document image and selfie using the webcam interface.

### Step 2: Backend Processing ⚙️
The FastAPI backend performs:
- **Image Storage** — Saves both images to audit folder
- **OCR on ID** — Extracts text using Tesseract
- **Face Comparison** — Generates embeddings and calculates similarity
- **Decision Scoring** — Applies risk rules and generates final decision

### Step 3: Audit Logging 📝
Each verification attempt receives a unique token with complete JSON metadata stored in:
```
audits/
  └── <token>/
      ├── id.jpg              # Original ID document
      ├── selfie.jpg          # User selfie
      ├── decision.json       # Final decision & score
      ├── extracted.json      # OCR results
      └── face.json           # Face matching data
```

### Step 4: Response Returned ✅
Frontend receives:
- ✓ Decision status (accepted/rejected)
- ✓ Similarity score
- ✓ Extracted text data
- ✓ Unique verification token

---

## 📁 Project Structure

```
kyc-system/
│
├── backend/
│   ├── app/
│   │   ├── api.py                  # API endpoints
│   │   ├── main.py                 # FastAPI app initialization
│   │   ├── decision_engine.py      # Risk scoring logic
│   │   ├── storage.py              # Audit storage handler
│   │   ├── utils.py                # Helper functions
│   │   └── model/                  # ML models & configs
│   ├── Dockerfile                  # Backend container config
│   └── requirements.txt            # Python dependencies
│
├── frontend/
│   ├── src/
│   │   ├── components/             # React components
│   │   ├── App.jsx                 # Main app component
│   │   ├── main.jsx                # Entry point
│   │   └── Style.css               # Styling
│   ├── dockerfile                  # Frontend container config
│   └── package.json                # Node dependencies
│
├── audits/                         # Generated audit logs (gitignored)
├── docker-compose.yml              # Container orchestration
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🛠️ Technology Stack

### Backend
- **FastAPI** — Modern, high-performance Python web framework
- **Tesseract OCR** — Text extraction from documents
- **face_recognition** — Face embedding and comparison
- **OpenCV** — Image processing
- **Pillow** — Image manipulation
- **Pydantic** — Data validation

### Frontend
- **React** — Component-based UI
- **Vite** — Fast build tool
- **react-webcam** — Camera integration
- **Axios** — HTTP client
- **CSS3** — Modern styling

### DevOps
- **Docker** — Containerization
- **Docker Compose** — Multi-container orchestration
- **Uvicorn** — ASGI server

---

## 🧪 API Reference

### `POST /api/verify`

**Endpoint:** `http://localhost:8000/api/verify`

**Description:** Submit ID document and selfie for verification

**Request Type:** `multipart/form-data`

**Parameters:**

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id_file` | File | ✅ Yes | ID document image (JPG/PNG) |
| `selfie_file` | File | ✅ Yes | User selfie image (JPG/PNG) |

**Example Request (cURL):**

```bash
curl -X POST "http://localhost:8000/api/verify" \
  -F "id_file=@/path/to/id.jpg" \
  -F "selfie_file=@/path/to/selfie.jpg"
```

**Example Response:**

```json
{
  "token": "2559e1f2-c50a-4049-9bc1-948bdbc5ecee",
  "decision": {
    "status": "accepted",
    "score": 0.82,
    "reason": "Face match confidence high"
  },
  "face": {
    "match": true,
    "similarity": 0.84,
    "threshold": 0.6
  },
  "extracted": {
    "lines": [
      "NAME: JOHN DOE",
      "COUNTRY: USA",
      "ID: 12345678",
      "EXPIRES: 2028"
    ],
    "confidence": 0.89
  },
  "audit_path": "audits/2559e1f2-c50a-4049-9bc1-948bdbc5ecee"
}
```

**Response Codes:**

| Code | Status | Description |
|------|--------|-------------|
| 200 | ✅ Success | Verification completed successfully |
| 400 | ❌ Bad Request | Missing files or invalid format |
| 500 | ⚠️ Server Error | Processing error |

### Interactive API Documentation

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI documentation.

---

## 💻 Local Development

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload --port 8000
```

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

---

## 🐛 Troubleshooting

<details>
<summary><strong>Backend unreachable / Connection refused</strong></summary>

**Solution:**
- Verify backend is running: `docker compose ps`
- Check port 8000 is not in use: `lsof -i :8000` (Mac/Linux) or `netstat -ano | findstr :8000` (Windows)
- Restart containers: `docker compose restart backend`
</details>

<details>
<summary><strong>CORS errors in browser console</strong></summary>

**Solution:**
- Ensure frontend fetch URL is `http://localhost:8000`
- Check `docker-compose.yml` has correct CORS_ORIGINS environment variable
- Restart both services after changes
</details>

<details>
<summary><strong>OCR returns empty or incorrect text</strong></summary>

**Solution:**
- Improve lighting when capturing ID
- Ensure ID is in focus and fills most of the frame
- Hold camera steady during capture
- Use high-resolution images (minimum 800x600)
- Avoid glare or shadows on document
</details>

<details>
<summary><strong>Face matching fails (low similarity)</strong></summary>

**Solution:**
- Use clear, frontal-facing selfie
- Ensure good lighting on face
- Remove glasses or hats if possible
- Face should be clearly visible in ID document
- Try multiple captures if first fails
</details>

<details>
<summary><strong>Docker compose constantly fails or hangs</strong></summary>

**Solution:**
```bash
# Stop and remove all containers
docker compose down -v

# Remove old images
docker compose down --rmi all

# Rebuild from scratch
docker compose up --build --force-recreate
```
</details>

<details>
<summary><strong>Permission denied errors on Linux</strong></summary>

**Solution:**
```bash
# Fix audit folder permissions
chmod -R 755 audits/

# Or run docker with sudo (not recommended for production)
sudo docker compose up --build
```
</details>

---

## 🔒 Security Considerations

⚠️ **Important Security Notes:**

- This is a **demonstration/prototype** system
- **Not production-ready** without additional hardening
- No authentication/authorization implemented
- File uploads are not sanitized for malicious content
- Stored data is not encrypted at rest

### For Production Use:

- [ ] Add authentication (JWT, OAuth2)
- [ ] Implement rate limiting
- [ ] Add file type validation and sanitization
- [ ] Encrypt stored images and data
- [ ] Use HTTPS only
- [ ] Implement proper access controls
- [ ] Add comprehensive logging
- [ ] Regular security audits
- [ ] Data retention policies

---

## 🛣️ Roadmap

### ✅ Current Features
- [x] Basic ID document capture
- [x] Selfie capture with webcam
- [x] OCR text extraction
- [x] Face matching algorithm
- [x] Simple risk scoring
- [x] Audit trail storage
- [x] Docker deployment

### 🚧 In Progress
- [ ] Multi-document type support (Passport, Driver's License, etc.)
- [ ] Better OCR parsing with field extraction
- [ ] Enhanced UI/UX with status indicators

### 🔮 Future Enhancements
- [ ] Machine learning-based fraud detection
- [ ] Liveness detection (anti-spoofing)
- [ ] Cloud-ready deployment modules (AWS, GCP, Azure)
- [ ] Mobile app support
- [ ] Multi-language OCR support
- [ ] Admin dashboard for verification review
- [ ] REST API authentication
- [ ] Webhook notifications
- [ ] Analytics and reporting

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/amazing-feature
   ```
5. **Open a Pull Request**

### Development Guidelines

- Follow existing code style
- Add tests for new features
- Update documentation as needed
- Keep commits atomic and well-described

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Yash Goyal**

- GitHub: [@Yashgoyal1875](https://github.com/Yashgoyal1875)
- Project: [kyc-system](https://github.com/Yashgoyal1875/kyc-system)

---

## 🙏 Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/) for blazing-fast API performance
- Powered by [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for text extraction
- Face recognition using [face_recognition](https://github.com/ageitgey/face_recognition) library
- Frontend built with [React](https://reactjs.org/) and [Vite](https://vitejs.dev/)

---

## 📊 Project Stats

![GitHub Stars](https://img.shields.io/github/stars/Yashgoyal1875/kyc-system?style=social)
![GitHub Forks](https://img.shields.io/github/forks/Yashgoyal1875/kyc-system?style=social)
![GitHub Issues](https://img.shields.io/github/issues/Yashgoyal1875/kyc-system)
![GitHub Last Commit](https://img.shields.io/github/last-commit/Yashgoyal1875/kyc-system)

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star!**

Built with ❤️ for the developer community

[Report Bug](https://github.com/Yashgoyal1875/kyc-system/issues) · [Request Feature](https://github.com/Yashgoyal1875/kyc-system/issues) · [Documentation](https://github.com/Yashgoyal1875/kyc-system/wiki)

</div>
