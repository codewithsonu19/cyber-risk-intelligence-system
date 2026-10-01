from fastapi import APIRouter
from pydantic import BaseModel, Field

from backend.services.investment_optimizer import (
    optimize_investments
)


router = APIRouter(
    prefix="/investment",
    tags=["Investment"]
)


class Investment(BaseModel):

    name: str

    category: str = ""

    cost: float = Field(
        ...,
        gt=0
    )

    risk_reduction: float = Field(
        ...,
        ge=0
    )


class OptimizationRequest(BaseModel):

    budget: float = Field(
        ...,
        ge=0
    )

    investments: list[Investment]


@router.post("/optimize")
def optimize(
    request: OptimizationRequest
):

    investments = [
        investment.model_dump()
        for investment in request.investments
    ]

    return optimize_investments(
        investments=investments,
        budget=request.budget
    )