# ── Base Image ────────────────────────────────────────────────
FROM python:3.12-slim

# ── Set Working Directory ─────────────────────────────────────
WORKDIR /app

# ── Copy Requirements First ───────────────────────────────────
COPY requirements.txt .

# ── Install Dependencies ──────────────────────────────────────
RUN pip install --no-cache-dir -r requirements.txt

# ── Copy App Code ─────────────────────────────────────────────
COPY . .

# ── Expose Port ───────────────────────────────────────────────
EXPOSE 8000

# ── Start Command ─────────────────────────────────────────────
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]