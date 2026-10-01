from pydantic import BaseModel, Field
from typing import Optional


class RiskCalculationRequest(BaseModel):

    asset_id: int

    vulnerability_id: Optional[int] = None

    likelihood: float = Field(
        ...,
        ge=0,
        le=1
    )

    impact: float = Field(
        ...,
        ge=0,
        le=10
    )


class RiskResult(BaseModel):

    asset_id: int

    vulnerability_id: Optional[int]

    likelihood: float

    impact: float

    risk_score: float

    risk_level: str