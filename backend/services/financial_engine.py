def calculate_sle(
    asset_value: float,
    exposure_factor: float
) -> float:
    """
    Single Loss Expectancy.

    SLE = Asset Value × Exposure Factor
    """

    asset_value = max(
        0,
        asset_value
    )

    exposure_factor = max(
        0,
        min(1, exposure_factor)
    )

    return round(
        asset_value * exposure_factor,
        2
    )


def calculate_ale(
    sle: float,
    annual_rate: float
) -> float:
    """
    Annualized Loss Expectancy.

    ALE = SLE × Annual Rate of Occurrence
    """

    annual_rate = max(
        0,
        annual_rate
    )

    return round(
        sle * annual_rate,
        2
    )


def calculate_financial_exposure(
    asset_value: float,
    exposure_factor: float,
    annual_rate: float
) -> dict:

    sle = calculate_sle(
        asset_value,
        exposure_factor
    )

    ale = calculate_ale(
        sle,
        annual_rate
    )

    return {
        "asset_value": asset_value,
        "exposure_factor": exposure_factor,
        "annual_rate": annual_rate,
        "sle": sle,
        "ale": ale
    }
def calculate_roi(
    risk_reduction: float,
    investment_cost: float
):
    if investment_cost <= 0:
        return 0

    roi = (
        (risk_reduction - investment_cost)
        / investment_cost
    ) * 100

    return round(roi, 2)