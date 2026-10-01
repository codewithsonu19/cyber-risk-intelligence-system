from fastapi import FastAPI

from backend.utils.database import (
    Base,
    engine
)

from backend.models.asset import Asset
from backend.models.vulnerability import Vulnerability

from backend.api.assets import (
    router as asset_router
)

from backend.api.vulnerabilities import (
    router as vulnerability_router
)

from backend.api.risk import (
    router as risk_router
)

from backend.api.financial import (
    router as financial_router
)

from backend.api.investment import (
    router as investment_router
)


Base.metadata.create_all(
    bind=engine
)


app = FastAPI(
    title="CyRIQ",
    description="Cyber Risk Intelligence & Quantification Platform",
    version="1.0.0"
)


app.include_router(
    asset_router
)

app.include_router(
    vulnerability_router
)

app.include_router(
    risk_router
)

app.include_router(
    financial_router
)

app.include_router(
    investment_router
)


@app.get("/")
def root():

    return {
        "application": "CyRIQ",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }