import pandas as pd


def load_data(file_path):
    data = pd.read_csv(file_path)
    return data


def prepare_data(file_path):
    data = load_data(file_path)

    features = [
        "likelihood",
        "impact",
        "asset_criticality",
        "cvss_score"
    ]

    X = data[features]
    y = data["risk_score"]

    return X, y