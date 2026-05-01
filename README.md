# Heart Disease Prediction API

An end-to-end Machine Learning project that predicts whether a patient
has heart disease based on 13 clinical features. Built with FastAPI,
containerized with Docker and deployed to AWS EC2 via AWS ECR.

---

## Live API
http://54.208.11.48:8000/docs

---

## Project Overview

A REST API that takes patient clinical data as input and returns
a heart disease prediction with confidence score. The model is trained
on the UCI Heart Disease dataset using Random Forest Classifier
achieving 84% accuracy.

---

## Tech Stack

| Layer | Technology |
|---|---|
| ML Model | Scikit-learn (Random Forest) |
| API Framework | FastAPI + Uvicorn |
| Containerization | Docker |
| Container Registry | AWS ECR |
| Cloud Server | AWS EC2 (Amazon Linux 2023) |
| Language | Python 3.12 |

---

## Project Structure
heart-disease-docker/
├── app/
│   ├── main.py          # FastAPI app and endpoints
│   ├── model.py         # Model loader and predictor
│   ├── schemas.py       # Pydantic input/output schemas
│   └── model.pkl        # Trained Random Forest model
├── train.py             # Model training script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image instructions
├── .dockerignore        # Files excluded from Docker
└── notes.md             # Project notes and documentation

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | / | Root - API status check |
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
  "prediction_label": "No Heart Disease",
  "confidence": 0.85
}
```

---

## Run Locally with Docker

```bash
# Build image
docker build -t heart-disease-api .

# Run container
docker run -p 8000:8000 heart-disease-api

# Open in browser
http://localhost:8000/docs
```

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
Built as part of an end-to-end ML engineering portfolio project.