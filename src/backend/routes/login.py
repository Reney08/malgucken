from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file, current_app
from werkzeug.security import check_password_hash
from ..database_interaction import get_user_by_username

import qrcode
import io


login_bp = Blueprint('login',
                     __name__,
                     url_prefix='/login',
                     template_folder='/src/frontend/templates/')

@login_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = get_user_by_username(username)
        if user and check_password_hash(user['password'], password):
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('main.main'))
        else:
            flash('Benutzername oder Passwort falsch!')
    return render_template('login/login.html')

@login_bp.route('/qr')
def login_qr():
    # erzeugt absolute URL, z.B. http://127.0.0.1:5000/login/
    login_url = url_for('login.login',
                        _external=True)
    img = qrcode.make(login_url)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    return send_file(buf, mimetype='image/png')

@login_bp.route('/gast-login')
def gast_login():
    session['logged_in'] = True
    session['username'] = 'Max Mustermann'
    session['is_guest'] = True  # Optional für weitere Beschränkungen
    return redirect(url_for('main.main'))
