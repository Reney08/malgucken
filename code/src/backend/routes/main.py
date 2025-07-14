from flask import Blueprint, render_template, request
from database_interaction import get_cocktails

from session_ueberpruefer import login_required

main_bp = Blueprint('main', __name__, url_prefix='/main')

@main_bp.route('/')
@login_required
def main():
    cocktails = get_cocktails()
    return render_template('main/main.html', cocktails=cocktails)

@main_bp.route('/cocktail_selected', methods=['GET', 'POST'])
@login_required
def cocktail_selected():
    data = request.get_json()
    name = data.get('name')
    print(f"Cocktail gewählt: {name}")  # Wird im Terminal ausgegeben!
    return '', 204  # Kein Inhalt zurückgeben