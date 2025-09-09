import RPi.GPIO as GPIO
import time

STEP = 17   # anpassen!
DIR = 27    # anpassen!
EN = 22     # anpassen!

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEP, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(EN, GPIO.OUT)

GPIO.output(EN, GPIO.LOW)   # Motor aktivieren (prüfen: evtl. HIGH nötig)
GPIO.output(DIR, GPIO.HIGH) # Richtung setzen

for _ in range(200):        # 200 Schritte
    GPIO.output(STEP, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(STEP, GPIO.LOW)
    time.sleep(0.001)

GPIO.cleanup()
