import pickle
import numpy as np
from app.schemas import PatientData, PredictionResult

# ── Load Model Once ───────────────────────────────────────────
with open("app/model.pkl", "rb") as f:
    model = pickle.load(f)

# ── Predict Function ──────────────────────────────────────────
def predict_heart_disease(data: PatientData) -> PredictionResult:
    
    # Convert input to numpy array in correct feature order
    features = np.array([[
        data.age,
        data.sex,
        data.cp,
        data.trestbps,
        data.chol,
        data.fbs,
        data.restecg,
        data.thalach,
        data.exang,
        data.oldpeak,
        data.slope,
        data.ca,
        data.thal
    ]])

    # Get prediction (0 or 1)
    prediction = int(model.predict(features)[0])

    # Get confidence score
    confidence = float(model.predict_proba(features)[0][prediction])

    # Human readable label
    label = "Heart Disease" if prediction == 1 else "No Heart Disease"

    return PredictionResult(
        prediction=prediction,
        prediction_label=label,
        confidence=round(confidence, 2)
    )