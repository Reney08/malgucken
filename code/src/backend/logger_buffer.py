from collections import deque

log_buffer = deque(maxlen=200)
sequence_running = False

def add_log(entry: str):
    log_buffer.append(entry)

def get_logs():
    return list(log_buffer)

def clear_logs():
    log_buffer.clear()

def set_sequence_running(state: bool):
    global sequence_running
    sequence_running = state

def is_sequence_running():
    return sequence_running
