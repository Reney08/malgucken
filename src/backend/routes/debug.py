# routes/debug.py

from flask import Blueprint, render_template, jsonify
from ..logger_buffer import get_logs

from ..logger_buffer import is_sequence_running

debug_bp = Blueprint('debug',
                     __name__,
                     url_prefix='/debug',
                     template_folder='/src/frontend/templates/')

@debug_bp.route('/logs')
def debug_logs():
    return render_template('/debug/logs.html')

@debug_bp.route('/logs/api')
def get_log_entries():
    logs = get_logs()
    return jsonify({
        'logs': logs,
        'running': is_sequence_running()
    })
