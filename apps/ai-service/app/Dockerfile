# 1) Base Python image
FROM python:3.13-alpine

WORKDIR /app

# 2) Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3) Copy source code
COPY ./main.py ./main.py

# 4) Expose port 8000 (FastAPI)
EXPOSE 8000

# 5) Entrypoint (we'll override with `dapr run` in development)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
