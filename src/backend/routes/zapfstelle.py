from ..database_interaction import get_all_zapfstellen, get_single_zapfstelle, set_zapfstelle, add_zapfstelle, delete_zapfstelle
from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_file, current_app

zapfstelle_bp = Blueprint('zapfstelle_bp',
                          __name__,
                          url_prefix='/zapfstelle',
                          template_folder='/src/frontend/templates/')

@zapfstelle_bp.route('/', methods=['GET', 'POST'])
def get_all_zapfstelle():
    zapfstelle = get_all_zapfstelle()
    render_template('zapfstelle/get_all.html')

@zapfstelle_bp.route('/get_single', methods=['GET', 'POST'])
def get_single_zapfstelle():
    zapfstelle = get_single_zapfstelle()
    render_template('zapfstelle/get_single.html')

@zapfstelle_bp.route('/set_zapfstelle', methods=['GET', 'POST'])
def set_zapfstelle():
    render_template('zapfstelle/set.html')

@zapfstelle_bp.route('/add_zapfstelle', methods=['GET', 'POST'])
def add_zapfstelle():
    render_template('zapfstelle/add.html')

@zapfstelle_bp.route('/delete_zapfstelle', methods=['GET', 'POST'])
def delete_zapfstelle():
    render_template('zapfstelle/delete.html')