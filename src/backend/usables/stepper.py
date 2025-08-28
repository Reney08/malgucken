#from logger_buffer import add_log

import time

# ▶ globaler Positionszähler
current_pos = 5000

# ▶ gibt aktuelle Position zurück
def get_current_position():
    #add_log(f"[CURRENT POS]: {current_pos}")
    return current_pos

# ▶ 1 Step nach links
def step_left():
    global current_pos
    current_pos -= 1
    # add_log(f"[STEPPER] ← Step Left: Position = {current_pos}")
    print(f"[STEPPER] ← Step Left: Position = {current_pos}")

# ▶ 1 Step nach rechts
def step_right():
    global current_pos
    current_pos += 1
    # add_log(f"[STEPPER] → Step Right: Position = {current_pos}")
    print(f"[STEPPER] → Step Right: Position = {current_pos}")

# ▶ gehe zu absoluter Zielposition
def move_to(target_pos):
    global current_pos
    if current_pos == target_pos:
        #add_log(f"[STEPPER] Already at {current_pos}, no move needed.")
        return

    #add_log(f"[STEPPER] Move from {current_pos} to {target_pos}...")
    while current_pos < target_pos:
        step_right()
        time.sleep(0.01)
    while current_pos > target_pos:
        step_left()
        time.sleep(0.01)
    #add_log(f"[STEPPER] Arrived at {current_pos}.")


# ▶ Referenzfahrt (Home)
def home_stepper():
    """Setzt Stepper auf Position 0 durch move_to(). Dann simuliert 10 Schritte Vorlauf."""
    print("[STEPPER] Starte Homing...")
    #add_log("[STEPPER] Starte Homing...")
    move_to(0)  # benutze logisches move_to für Homing

    #add_log("[STEPPER] Referenz erreicht (0). Warte 1 Sekunde...")
    print("[STEPPER] Referenz erreicht (0). Warte 1 Sekunde...")
    #time.sleep(1)

    #add_log("[STEPPER] Kalibriere... Gehe 10 Schritte nach rechts.")
    print("[STEPPER] Kalibriere... Gehe 10 Schritte nach rechts.")
    move_to(10)

    #add_log(f"[STEPPER] Homing abgeschlossen. Aktuelle Position: {current_pos}")
    print(f"[STEPPER] Homing abgeschlossen. Aktuelle Position: {current_pos}")
