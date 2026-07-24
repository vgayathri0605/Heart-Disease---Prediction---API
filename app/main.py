from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import PatientData, PredictionResult
from app.model import predict_heart_disease

# ── Create FastAPI App ────────────────────────────────────────
app = FastAPI(
    title="Heart Disease Prediction API",
    description="Predicts whether a patient has heart disease based on 13 clinical features",
    version="1.0.0"
)

# ── CORS Middleware ───────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # allows frontend HTML page to call the API
    allow_methods=["*"],        # allows GET, POST etc
    allow_headers=["*"],        # allows all headers
)

# ── Root Endpoint ─────────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "Heart Disease Prediction API is running"}

# ── Health Check ──────────────────────────────────────────────
@app.get("/health")
def health():
    return {"status": "healthy"}

# ── Prediction Endpoint ───────────────────────────────────────
@app.post("/predict", response_model=PredictionResult)
def predict(data: PatientData):
    result = predict_heart_disease(data)
    return result


