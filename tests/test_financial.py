from backend.services.financial_engine import calculate_roi


def test_roi():
    result = calculate_roi(9, 2)

    assert result == 350.0