# usables/servo.py
from logger_buffer import add_log

def dispense_servo(amount):
    # print(f"[SERVO] Dispensing {amount}ml at this position (platform stationary)")
    add_log(f"[SERVO] Dispensing {amount}ml at this position (platform stationary)")
    # Your servo PWM logic goes here
