from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.utils.database import get_db
from backend.models.vulnerability import Vulnerability


router = APIRouter(
    prefix="/vulnerabilities",
    tags=["Vulnerabilities"]
)


@router.get("/")
def get_vulnerabilities(
    db: Session = Depends(get_db)
):

    return db.query(Vulnerability).all()


@router.post("/")
def create_vulnerability(
    asset_id: int,
    name: str,
    severity: float,
    exploitability: float,
    db: Session = Depends(get_db)
):

    vulnerability = Vulnerability(
        asset_id=asset_id,
        name=name,
        severity=severity,
        exploitability=exploitability
    )

    db.add(vulnerability)

    db.commit()

    db.refresh(vulnerability)

    return vulnerability