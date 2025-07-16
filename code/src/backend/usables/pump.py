# usables/pump.py
from logger_buffer import add_log

def dispense_pump(amount, pwm_channel):
    # print(f"[PUMP] Dispensing {amount}ml using pump at channel {pwm_channel}")
    add_log(f"[PUMP] Dispensing {amount}ml using pump at channel {pwm_channel}")
    # Your pump control logic (GPIO or relay activation) here
