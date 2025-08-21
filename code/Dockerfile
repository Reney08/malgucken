FROM python:3.11-slim

# System-Abhängigkeiten für mariadb & RPi.GPIO
RUN apt-get update && apt-get install -y \
    python3-rpi.gpio \
    libmariadb-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# requirements zuerst kopieren, damit Docker-Cache genutzt wird
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
