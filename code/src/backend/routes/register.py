from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash
from database_interaction import safe_login_data

register_bp = Blueprint('register', __name__, url_prefix='/register', template_folder='../../frontend/templates')

@register_bp.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        terms_accepted = request.form.get('terms') == 'on'
        if not terms_accepted:
            flash('Bitte Nutzungsbedingungen akzeptieren!')
            return render_template('register/register.html')
        hashed_pw = generate_password_hash(password)
        safe_login_data(username, hashed_pw, terms_accepted)
        flash('Registrierung erfolgreich! Bitte logge dich ein.')
        return redirect(url_for('login.login'))
    return render_template('register/register.html')
