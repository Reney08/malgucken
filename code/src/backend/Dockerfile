FROM python:3.11-slim

# benötigte Systempakete für RPi GPIO
RUN apt-get update && apt-get isntall -y gcc python3-dev

RUN apt-get update && apt-get install -y \
    python3-rpi.gpio \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . /app

# Python-Abhängigkeiten (falls requirements.txt existiert)
RUN pip install --no-cache-dir -r requirements.txt

# Flask starten
CMD ["python", "app.py"]
