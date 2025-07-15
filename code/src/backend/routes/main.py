from flask import Blueprint, render_template, request
from database_interaction import get_cocktails, get_cocktail_by_name, get_ingredients_for_cocktail

from session_ueberpruefer import login_required

main_bp = Blueprint('main', __name__, url_prefix='/main')

@main_bp.route('/')
@login_required
def main():
    cocktails = get_cocktails()
    return render_template('main/main.html', cocktails=cocktails)

@main_bp.route('/cocktail/<cocktail_name>')
@login_required
def cocktail_detail(cocktail_name):
    cocktail = get_cocktail_by_name(cocktail_name)
    zutaten = get_ingredients_for_cocktail(cocktail_name)
    if not cocktail:
        return "Cocktail nicht gefunden", 404
    return render_template('main/selected_cocktail.html', cocktail=cocktail, zutaten=zutaten)
