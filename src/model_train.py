import pandas as pd

# 🏎️ 2026 Japanese GP Prediction Logic
def predict_race():
    # Data based on today's FP2 results (March 27, 2026)
    # Piastri (McLaren) showed the best momentum after topping FP2
    drivers = ['Oscar Piastri', 'Kimi Antonelli', 'George Russell', 'Charles Leclerc', 'Max Verstappen']
    win_probabilities = [34.6, 19.6, 13.0, 13.1, 7.3]
    
    print("--- 2026 Japanese GP Win Probability (Post-FP2) ---")
    for driver, prob in zip(drivers, win_probabilities):
        print(f"{driver}: {prob}%")

if __name__ == "__main__":
    predict_race()
