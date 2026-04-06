from pydantic import BaseModel

# ── Input Schema ──────────────────────────────────────────────
class PatientData(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# ── Output Schema ─────────────────────────────────────────────
class PredictionResult(BaseModel):
    prediction: int
    prediction_label: str
    confidence: float