# 🏎️ GrandPrix-Oracle: 2026 Japanese GP Prediction
A Machine Learning project to predict the winner of the 2026 Japanese Grand Prix at Suzuka, using real-time practice data.

## 🌟 The Problem
2026 introduced new "Active Aero" and "Boost Mode" regulations. Predicting winners requires analyzing how cars adapt their aerodynamics between high-speed corners and straights.

## 🛠️ How it Works
1. **Data Ingestion:** Uses FastF1 API to pull FP1 and FP2 telemetry.
2. **Feature Engineering:** Calculates "Momentum" (Position gain between sessions).
3. **Modeling:** Uses **XGBoost** to rank driver performance.

## 📊 Latest Prediction (Friday, March 27, 2026)
Based on today's FP2 where Oscar Piastri broke the Mercedes streak:
- **Oscar Piastri:** 34.6% (Favorite)
- **Kimi Antonelli:** 19.6%
- **George Russell:** 13.0%
