# 🏎️ Japanese Grand Prix 2026: ML Prediction Engine
An AI-powered system designed to predict the winner of the 2026 Japanese GP at Suzuka using real-time FP1 and FP2 telemetry.

## 🌟 Project Overview
This project uses **XGBoost** and **Monte Carlo Simulations** to analyze driver momentum and car performance under the 2026 "Active Aero" regulations.

## 🛠️ The Logic
- **Data Ingestion:** Fetching live lap times from Suzuka.
- **Feature Engineering:** Calculating "Momentum" (Performance jump from FP1 to FP2).
- **Simulation:** Running the race 10,000 times to find the win probability.

## 📊 Current Prediction (Post-FP2)
- **Oscar Piastri (McLaren):** 34.6%
- **Kimi Antonelli (Mercedes):** 19.6%
