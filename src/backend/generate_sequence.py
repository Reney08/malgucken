import math
from database_interaction import (
    get_ingredients_for_cocktail,
    get_pumps_from_db,
    get_servo_positions_from_db
)

def create_cocktail_sequence(cocktail_name, initial_weight=0):
    sequence = []
    ingredients = get_ingredients_for_cocktail(cocktail_name)
    if not ingredients:
        raise ValueError(f"Cocktail '{cocktail_name}' not found in recipes.")

    pumps = get_pumps_from_db()
    servos = get_servo_positions_from_db()

    pump_lookup = {v['liquid'].lower(): v for v in pumps.values()}
    servo_lookup = {v['liquid'].lower(): v for v in servos.values()}

    current_weight = initial_weight

    for ing in ingredients:
        name = ing["Zutat"]
        amount = ing["Menge"]
        name_lc = name.lower()

        if name_lc in pump_lookup:
            pump = pump_lookup[name_lc]
            target_weight = current_weight + amount

            sequence.append({
                "type": "pump",
                "action": "dispense",
                "details": {
                    "liquid": name,
                    "amount": amount,
                    "pwm_channel": pump["pwm_channel"],
                    "weight_target": target_weight
                }
            })
            current_weight = target_weight

        elif name_lc in servo_lookup:
            pos = servo_lookup[name_lc]
            full_units = amount // 25
            leftover = amount % 25
            for _ in range(full_units):
                sequence.append({
                    "type": "servo",
                    "action": "dispense",
                    "details": {
                        "liquid": name,
                        "amount": 25,
                        "steps": pos['steps']
                    },
                    "time_delay": 10
                })
            if leftover > 0:
                sequence.append({
                    "type": "servo",
                    "action": "dispense",
                    "details": {
                        "liquid": name,
                        "amount": leftover,
                        "steps": pos['steps']
                    },
                    "time_delay": 10
                })
        else:
            raise ValueError(f"Ingredient '{name}' not mapped to any pump or servo position.")
    return sequence
