from flask import Flask, redirect, session
from routes import *
app = Flask(__name__,
            template_folder='../frontend/templates',
            static_folder='../frontend/static'
            )
app.secret_key = 'supergeheimer_schluessel_1234567890'

@app.route('/')
def index():
    return redirect('/login')

@app.route('/logout', methods=['get', 'post'])
def logout():
    session.clear()
    return redirect('/login')

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)
app.register_blueprint(main_bp)
app.register_blueprint(debug_bp)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
