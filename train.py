import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle
import urllib.request

# ── 1. Load Dataset ───────────────────────────────────────────
url = "https://raw.githubusercontent.com/sharmaroshan/Heart-UCI-Dataset/master/heart.csv"
df = pd.read_csv(url)

print(f"Dataset shape: {df.shape}")
print(df.head())

# ── 2. Prepare Features & Target ─────────────────────────────
X = df.drop("target", axis=1)
y = df["target"]

# ── 3. Train/Test Split ───────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── 4. Train Model ────────────────────────────────────────────
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ── 5. Evaluate ───────────────────────────────────────────────
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy:.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ── 6. Save Model ─────────────────────────────────────────────
with open("app/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\nModel saved to app/model.pkl")