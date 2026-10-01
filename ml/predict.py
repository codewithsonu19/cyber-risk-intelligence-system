import pickle


def predict_risk(criticality, cvss_score, likelihood):

    with open("ml/model.pkl", "rb") as file:
        model = pickle.load(file)

    prediction = model.predict([
        [criticality, cvss_score, likelihood]
    ])

    return round(float(prediction[0]), 2)