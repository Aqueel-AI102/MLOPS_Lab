import pandas as pd
import numpy as np
from src.sweep_experiments import run_parameter_sweep, identify_best_run
from sklearn.model_selection import train_test_split
import joblib
import json
import sys
import os

# Add project root to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Starting MLflow experiment sweep...")

# Load clean data
ratings_df = pd.read_csv('data/processed/ratings_clean.csv')

# Load features
features = joblib.load('models/rating_features.pkl')

# Target: avg rating per user
y = ratings_df.groupby('user_id')['rating'].mean()

# Split users
train_users, test_users = train_test_split(
    features.user_ids,
    test_size=0.2,
    random_state=42
)

# Create datasets
X_train = features.ratings_matrix.loc[train_users].values
X_test = features.ratings_matrix.loc[test_users].values
y_train = pd.DataFrame({'rating': y.loc[train_users].values})
y_test = pd.DataFrame({'rating': y.loc[test_users].values})

# Sweep
k_values = [3, 5, 10, 15, 20]
results = run_parameter_sweep(
    k_values=k_values,
    X_train=X_train,
    X_test=X_test,
    y_train=y_train,
    y_test=y_test,
    experiment_name="movielens_knn_sweep"
)

# Best result
best_k, best_result = identify_best_run(results, metric="rmse")

print("\n" + "="*60)
print(f"Best K: {best_k}")
print(f"RMSE: {best_result['rmse']:.3f}")
print(f"MAE: {best_result['mae']:.3f}")
print(f"Coverage: {best_result['coverage']:.1%}")
print(f"Run ID: {best_result['run_id']}")
print("="*60)

# Save results
with open('evaluations/experiment_sweep_results.json', 'w') as f:
    json.dump({str(k): result for k, result in results.items()}, f, indent=2)

print("✓ Results saved")