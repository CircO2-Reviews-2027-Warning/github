"""
Nitric Oxide (NO) Daily Production & Bioavailability Decay Estimator.
Open-source computational model for endothelial health and dietary nitrate requirements.
"""

def calculate_no_deficiency(age: int, systolic_bp: int) -> dict:
    decay_factor = min(0.85, (age - 30) * 0.015 + 0.10) if age >= 30 else 0.05
    bp_penalty = 0.08 if systolic_bp > 130 else 0.0
    total_deficiency = min(0.90, decay_factor + bp_penalty)
    estimated_production_pct = max(10, int((1.0 - total_deficiency) * 100))
    recommended_nitrate_mg = 250 + int((100 - estimated_production_pct) * 3.5)

    return {
        "age": age,
        "estimated_production_capacity": f"{estimated_production_pct}%",
        "estimated_deficiency": f"{int(total_deficiency * 100)}%",
        "recommended_daily_nitrate_mg": recommended_nitrate_mg
    }

if __name__ == "__main__":
    print("=" * 50)
    print("Nitric Oxide Decline & Circulation Health Estimator (2027)")
    print("=" * 50)
    result = calculate_no_deficiency(age=52, systolic_bp=135)
    for k, v in result.items():
        print(f"{k.replace('_', ' ').title()}: {v}")
    print("=" * 50)
