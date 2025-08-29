from flask import Blueprint, render_template, request, redirect, url_for
from database_interaction import get_cocktails, get_cocktail_by_name, get_ingredients_for_cocktail
from generate_sequence import create_cocktail_sequence
from session_ueberpruefer import login_required
from execute_sequence import execute_sequence
from usables.stepper import move_to
# from logger_buffer import add_log

# from execute_sequence import start_sequence_thread

main_bp = Blueprint('main',
                    __name__,
                    url_prefix='/main',
                    template_folder='/src/frontend/templates/')

@main_bp.route('/')
@login_required
def main():
    # add_log("on main page")
    cocktails = get_cocktails()
    move_to(5000)
    # add_log(f"{len(cocktails)} cocktails found")
    return render_template('/main/main.html', cocktails=cocktails)

@main_bp.route('/cocktail/<cocktail_name>', methods=['GET', 'POST'])
@login_required
def cocktail_detail(cocktail_name: str):
    cocktail = get_cocktail_by_name(cocktail_name)
    # add_log(f"on page: {cocktail}")

    zutaten = get_ingredients_for_cocktail(cocktail_name)
    # add_log(f"{len(zutaten)} ingredients found")

    if not cocktail:
        # add_log(f"no Cocktail found with this name: {cocktail}")
        return "Cocktail nicht gefunden", 404

    if request.method == 'POST':
        try:
            sequence = create_cocktail_sequence(cocktail_name)
            print("\n--- Sequence Created ---\n")
            # add_log("\n--- Sequence Created ---\n")

            for i, step in enumerate(sequence, 1):
                print(f"Step {i}: {step}")
                # add_log(f"Step {i}: {step}")

            # add_log("\n--- Sequence Completed ---\n")
            execute_sequence(sequence)
            # ✅ Redirect zur Hauptauswahlseite nach erfolgreicher Zubereitung

            return redirect(url_for('main.main'))

        except Exception as e:
            print(f"Fehler beim Erzeugen der Sequenz: {e}")
            # add_log(f"Fehler beim Erzeugen der Sequenz: {e}")
            # Optional: Du könntest hier auch redirecten mit Fehler-Info

            return redirect(url_for('main.cocktail_detail', cocktail_name=cocktail_name))

    # Wenn GET
    return render_template(
        '/main/selected_cocktail.html',
        cocktail=cocktail,
        zutaten=zutaten
    )

