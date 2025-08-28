FROM python:3.11-bullseye

# Arbeitsverzeichnis setzen
WORKDIR .

# benötigte Systempakete für RPi GPIO
RUN apt-get update && apt-get install -y \
    gcc \
    cmake \
    git  \
    libssl-dev \
    make  \
    pkg-config \
    python3-dev \
    # python3-rpi.gpio \
    && rm -rf /var/lib/apt/lists/*

# installiert MariaDB Connector/C >= 3.3.1 manuell da sonst Fehlermeldung
RUN git clone https://github.com/mariadb-corporation/mariadb-connector-c.git \
    && cd mariadb-connector-c \
    && git checkout v3.3.3 \
    && cmake . \
    && make \
    && make install \
    && ldconfig \
    && cd .. \
    && rm -rf mariadb-connector-c

# Requirements installieren
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Flask-App kopieren
COPY . .

# Flask starten
CMD ["python", "app.py"]
