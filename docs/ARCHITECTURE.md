# Architecture

The project is organized as a small data and machine-learning pipeline:

1. Fetch observations into `data/raw/`.
2. Validate and transform them into `data/interim/` and `data/processed/`.
3. Build features and train baseline or LightGBM models.
4. Evaluate models and save metrics, figures, and model artifacts.
5. Estimate the probability that a daily maximum temperature reaches a configured threshold.

The package implementation lives in `src/weather_ai/`; runnable workflow entry points belong in `scripts/`.
