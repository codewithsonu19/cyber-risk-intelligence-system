def calculate_risk(
    criticality: float,
    cvss: float,
    likelihood: float,
    estimated_loss: float
):
    # Financial risk exposure
    risk_exposure = estimated_loss * likelihood

    # Overall risk score
    risk_score = (
        criticality * 0.4
        + cvss * 0.4
        + likelihood * 10 * 0.2
    )

    # Risk level
    if risk_score >= 7:
        risk_level = "High"
    elif risk_score >= 4:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    return {
        "risk_score": round(risk_score, 2),
        "risk_exposure": round(risk_exposure, 2),
        "risk_level": risk_level
    }
def calculate_asset_risk(
    criticality: float,
    cvss: float,
    likelihood: float,
    estimated_loss: float
):
    return calculate_risk(
        criticality,
        cvss,
        likelihood,
        estimated_loss
    )