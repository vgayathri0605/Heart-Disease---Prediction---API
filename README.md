# Heart Disease Prediction API

An end-to-end Machine Learning project that predicts whether a patient
has heart disease based on 13 clinical features. Built with FastAPI,
containerized with Docker, deployed to AWS EC2 via AWS ECR, with a
CI/CD pipeline and a user-friendly frontend.

---

## Live API
http://54.208.11.48:8000/docs

---

## Project Overview

A REST API that takes patient clinical data as input and returns
a heart disease prediction with confidence score. The model is trained
on the UCI Heart Disease dataset using Random Forest Classifier
achieving 84% accuracy.

Includes a frontend designed for both doctors and common users —
with plain English labels, medical terms, and helpful hints for every field.

---

## Tech Stack

| Layer | Technology |
|---|---|
| ML Model | Scikit-learn (Random Forest) |
| API Framework | FastAPI + Uvicorn |
| Containerization | Docker |
| Container Registry | AWS ECR |
| Cloud Server | AWS EC2 (Amazon Linux 2023) |
| CI/CD | GitHub Actions |
| Frontend | HTML, CSS, Vanilla JavaScript |
| Language | Python |

---

## Project Structure

```
heart-disease-docker/
├── app/
│   ├── main.py          # FastAPI app, endpoints and CORS
│   ├── model.py         # Model loader and predictor
│   ├── schemas.py       # Pydantic input/output schemas
│   └── model.pkl        # Trained Random Forest model
├── .github/
│   └── workflows/
│       └── deploy.yml   # CI/CD pipeline — auto deploy on push
├── index.html           # Frontend for users and doctors
├── train.py             # Model training script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image instructions
└── .dockerignore        # Files excluded from Docker
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Root — API status check |
| GET | /health | Health check for monitoring |
| POST | /predict | Heart disease prediction |

---

## Input Features

| Feature | Type | Description |
|---|---|---|
| age | int | Age of patient |
| sex | int | Sex (1=male, 0=female) |
| cp | int | Chest pain type (0-3) |
| trestbps | int | Resting blood pressure |
| chol | int | Serum cholesterol (mg/dl) |
| fbs | int | Fasting blood sugar > 120 (1=yes) |
| restecg | int | Resting ECG results (0-2) |
| thalach | int | Max heart rate achieved |
| exang | int | Exercise induced angina (1=yes) |
| oldpeak | float | ST depression by exercise |
| slope | int | Slope of peak exercise ST |
| ca | int | Number of major vessels (0-3) |
| thal | int | Thalassemia type (0-3) |

---

## Sample Request

```json
{
  "age": 52,
  "sex": 1,
  "cp": 0,
  "trestbps": 125,
  "chol": 212,
  "fbs": 0,
  "restecg": 1,
  "thalach": 168,
  "exang": 0,
  "oldpeak": 1.0,
  "slope": 2,
  "ca": 2,
  "thal": 3
}
```

## Sample Response

```json
{
  "prediction": 0,
  "probability": 0.1200,
  "result": "No heart disease detected"
}
```

---

## CI/CD Pipeline

Every push to `main` branch automatically:

1. Checks out code on a free GitHub Ubuntu machine
2. Logs into AWS using GitHub Secrets
3. Builds a new Docker image
4. Tags it with commit SHA and `latest`
5. Pushes both tags to AWS ECR

GitHub Secrets required:
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_REGION`

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/vgayathri0605/Heart-Disease---Prediction---API.git
cd Heart-Disease---Prediction---API

# Create virtual environment
py -m venv venv
venv\Scripts\activate

# Install dependencies
py -m pip install -r requirements.txt

# Start API
py -m uvicorn app.main:app --reload

# Open Swagger UI
http://127.0.0.1:8000/docs
```

---

## Run with Docker

```bash
# Build image
docker build -t heart-disease-api .

# Run container
docker run -p 8000:8000 heart-disease-api

# Open in browser
http://localhost:8000/docs
```

---

## Frontend

Open `index.html` with Live Server in VS Code.

Designed for both audiences:
- Common users — plain English labels with helpful hints
- Doctors — medical terms shown beside each label

Shows result with probability percentage and animated risk gauge.

---

## Dataset

- **Name:** UCI Heart Disease Dataset (Cleveland)
- **Source:** UCI Machine Learning Repository
- **Features:** 13 clinical features
- **Target:** Binary classification (0 = No Disease, 1 = Disease)
- **Model:** Random Forest Classifier
- **Accuracy:** 84%

---

## Author

Gayathri V
[GitHub](https://github.com/vgayathri0605)

---

## Disclaimer

This tool is for educational and awareness purposes only.
Always consult a qualified doctor for medical advice.