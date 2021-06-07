from dataclasses import dataclass
import datetime
from app import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


@dataclass
class Location(db.Model):
    id: UUID(as_uuid=True)
    name: str
    longitude: float
    latitude: float
    full_address: str
    zone_id: UUID(as_uuid=True)
    modified: str
    created: str
    __tablename__ = "location"
    __table_args__ = {"extend_existing": True}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(60), unique=True, nullable=True)
    longitude = db.Column(db.Numeric, nullable=True)
    latitude = db.Column(db.Numeric, nullable=True)
    full_address = db.Column(db.String, nullable=True)
    zone_id = db.Column(UUID(as_uuid=True), db.ForeignKey("zone.id"), nullable=True)
    modified = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
