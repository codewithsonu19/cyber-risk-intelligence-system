from backend.services.risk_engine import calculate_risk


def test_risk_calculation():
    result = calculate_risk(9, 9.8, 0.6, 20)

    assert result["risk_exposure"] == 12.0
    assert result["risk_level"] == "High"