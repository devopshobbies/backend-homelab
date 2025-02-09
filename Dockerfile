FROM python:3.10-slim-bookworm

RUN apt-get update --fix-missing && apt-get install -y --fix-missing \
    build-essential \
    gcc \
    g++ \
    libpq5 \
    python3-dev \
    libssl-dev

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt

CMD ["uvicorn", "fastapi_backend_app:app", "--host", "0.0.0.0"]