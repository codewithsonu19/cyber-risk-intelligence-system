from sqlalchemy import Column, Integer, String, Float

from backend.utils.database import Base


class Asset(Base):

    __tablename__ = "assets"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    asset_type = Column(
        String,
        nullable=False
    )

    criticality = Column(
        Float,
        default=1.0
    )

    value = Column(
        Float,
        default=0.0
    )