# Module 01 — Exercise 3
def temperature_label(t: float) -> str:
    if not 0.0 <= t <= 1.0:
        raise ValueError("temperature must be between 0.0 and 1.0")
    if t <= 0.3:
        return "precise"
    if t <= 0.7:
        return "balanced"
    return "creative"


for value in [0.0, 0.3, 0.5, 0.7, 0.9, 1.0]:
    print(f"{value:.1f} -> {temperature_label(value)}")

try:
    temperature_label(1.2)
except ValueError as error:
    print(f"Error: {error}")
