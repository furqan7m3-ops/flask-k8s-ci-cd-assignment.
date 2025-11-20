# syntax=docker/dockerfile:1


# --- Builder stage: install dependencies ---
FROM python:3.11-slim AS builder
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --upgrade pip \
&& pip install --prefix=/install -r requirements.txt


# --- Final stage: copy runtime files ---
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
