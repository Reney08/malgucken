FROM python:3.11-slim

# Arbeitsverzeichnis setzen
WORKDIR .

# benötigte Systempakete für RPi GPIO
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    python3-dev

RUN apt-get update && apt-get install -y \
    python3-rpi.gpio \
    && rm -rf /var/lib/apt/lists/*

# Requirements installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Flask-App kopieren
COPY . .

# Flask starten
CMD ["python", "app.py"]
