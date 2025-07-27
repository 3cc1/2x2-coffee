# coffee_logic.py

def recommend_coffee(age, weight, sleep_hours, study_hours, caffeine_tolerance):
    base_caffeine = 5
    total_mg = weight * base_caffeine

    if sleep_hours < 8:
        total_mg *= 1.2
    if study_hours > 4:
        total_mg += 50

    coffee_size = "Small"
    if total_mg > 250:
        coffee_size = "Large"
    elif total_mg > 150:
        coffee_size = "Medium"

    return {
        "caffeine_mg": round(total_mg),
        "recommended_size": coffee_size,
        "sugar_level": "Low" if caffeine_tolerance == "high" else "Medium",
        "espresso_shots": 1 if total_mg < 150 else (2 if total_mg < 300 else 3)
    }