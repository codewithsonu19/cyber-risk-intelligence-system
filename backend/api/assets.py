from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.utils.database import get_db
from backend.models.asset import Asset


router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


@router.get("/")
def get_assets(
    db: Session = Depends(get_db)
):
    return db.query(Asset).all()


@router.post("/")
def create_asset(
    name: str,
    asset_type: str,
    criticality: float,
    value: float,
    db: Session = Depends(get_db)
):

    asset = Asset(
        name=name,
        asset_type=asset_type,
        criticality=criticality,
        value=value
    )

    db.add(asset)
    db.commit()
    db.refresh(asset)

    return asset