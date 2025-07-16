from logger_buffer import set_sequence_running
from usables.stepper import move_to, home_stepper
from usables.servo import dispense_servo
from usables.pump import dispense_pump
from usables.station_positions import get_pump_pos, get_outlet_pos
from logger_buffer import add_log

import time
import threading

def start_sequence_thread(sequence):
    def run_sequence():
        execute_sequence(sequence)
    thread = threading.Thread(target=run_sequence)
    thread.start()

def execute_sequence(sequence):
    set_sequence_running(True)
    try:
        add_log("👉 Sequence started...")
    finally:
        set_sequence_running(False)

    # print("[EXECUTOR] Homing Stepper...")
    add_log("[EXECUTOR] Homing Stepper...")
    home_stepper()  # Z.B. am Anfang der Funktion aufrufen

    for i, step in enumerate(sequence, 1):
        # print(f"\n==> Step {i}: {step}")
        add_log(f"\n==> Step {i}: {step}")
        if step['type'] == 'pump':
            channel = step['details']['pwm_channel']
            amount = step['details']['amount']
            pump_pos = get_pump_pos(channel)
            if pump_pos is None:
                raise Exception(f"No position for pump channel {channel}")
            move_to(pump_pos)
            dispense_pump(amount, channel)
            add_log(f"[PUMP] Dispensing {amount}ml using pump at channel {channel}")

        elif step['type'] == 'servo':
            outlet_pos = get_outlet_pos()
            if outlet_pos is None:
                raise Exception("No outlet position configured")
            move_to(outlet_pos)
            amount = step['details']['amount']
            dispense_servo(amount)
            if 'time_delay' in step:
                print(f"Waiting {step['time_delay']}s for refill...")
                time.sleep(step['time_delay'])
            add_log(f"[SERVO] Dispensing {amount}ml at this position (platform stationary)")

        else:
            print(f"Unknown step type: {step['type']}")

    move_to(5000)
    print("[EXECUTOR] moving Stepper to get glass out of sequence...")
    time.sleep(5)
