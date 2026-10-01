from fastapi import APIRouter
from pydantic import BaseModel, Field

from backend.services.financial_engine import (
    calculate_financial_exposure
)


router = APIRouter(
    prefix="/financial",
    tags=["Financial"]
)


class FinancialRequest(BaseModel):

    asset_value: float = Field(
        ...,
        ge=0
    )

    exposure_factor: float = Field(
        ...,
        ge=0,
        le=1
    )

    annual_rate: float = Field(
        ...,
        ge=0
    )


@router.post("/exposure")
def financial_exposure(
    request: FinancialRequest
):

    return calculate_financial_exposure(
        asset_value=request.asset_value,
        exposure_factor=request.exposure_factor,
        annual_rate=request.annual_rate
    )