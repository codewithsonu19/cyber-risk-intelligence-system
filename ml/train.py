import os
import joblib
from sklearn.ensemble import RandomForestRegressor

from preprocessing import prepare_data


DATA_PATH = os.path.join(
    os.path.dirname(__file__),
    "data",
    "training_data.csv"
)

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "model.pkl"
)


X, y = prepare_data(DATA_PATH)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, MODEL_PATH)

print("Model trained successfully!")
print("Model saved at:", MODEL_PATH)