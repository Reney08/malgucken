# usables/station_positions.py
from logger_buffer import add_log
from database_interaction import get_station_positions

# Load on module import
_station_positions = get_station_positions()

def get_station_positions_map():
    add_log(f"[STATION POSITIONS]: {station_positions}")
    return _station_positions

def get_pump_pos(pwm_channel):
    add_log(f"[PUMP POS]: {pwm_channel}")
    return _station_positions.get(f'pump_{pwm_channel}')

def get_outlet_pos():
    add_log(f"[OUTLET POS]: {get_pump_pos()}")
    return _station_positions.get('outlet')

# print("[Station Map] Loaded:", _station_positions)
# add_log(f"[PUMP POS]: {get_pump_pos()}")
