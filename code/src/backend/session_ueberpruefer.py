from functools import wraps
from flask import session, redirect, url_for

def login_required(view):
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login.login'))  # Passe ggf. den Namen deines Login-Blueprints an!
        return view(*args, **kwargs)
    return wrapped_view
