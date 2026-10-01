from fastapi import APIRouter

from backend.models.risk import (
    RiskCalculationRequest
)

from backend.services.risk_engine import (
    calculate_risk,
    calculate_asset_risk
)


router = APIRouter(
    prefix="/risk",
    tags=["Risk"]
)


@router.post("/calculate")
def calculate(
    request: RiskCalculationRequest
):

    result = calculate_risk(
        likelihood=request.likelihood,
        impact=request.impact
    )

    return {
        "asset_id": request.asset_id,
        "vulnerability_id": request.vulnerability_id,
        **result
    }


@router.post("/asset-risk")
def calculate_asset(
    request: RiskCalculationRequest
):

    # Temporary value.
    # Later we will automatically fetch
    # asset criticality from database.

    criticality = 5

    result = calculate_asset_risk(
        criticality=criticality,
        likelihood=request.likelihood,
        impact=request.impact
    )

    return {
        "asset_id": request.asset_id,
        "vulnerability_id": request.vulnerability_id,
        **result
    }