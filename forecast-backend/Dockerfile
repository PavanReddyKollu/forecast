# ───────────────────────────────────────────────────────────────
#  FastAPI Dockerfile
# ───────────────────────────────────────────────────────────────
FROM python:3.11-slim AS base

# set workdir
WORKDIR /app

# prevent Python buffering (so logs show up immediately)
ENV PYTHONUNBUFFERED=1

# Install runtime dependencies
# COPY requirements.txt .
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code

# Expose Uvicorn port
EXPOSE 8000

# Run Uvicorn via your worker.py entrypoint
CMD ["uvicorn", "worker:app", "--host", "0.0.0.0", "--port", "8000"]
