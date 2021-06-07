from dataclasses import dataclass
import datetime
from app import db
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


@dataclass
class Zone(db.Model):
    id: UUID(as_uuid=True)
    name: str
    wave_points: float
    modified: str
    created: str
    __tablename__ = "zone"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(60), unique=True, nullable=False)
    wave_points = db.Column(db.Numeric, unique=True, nullable=False)
    locations = db.relationship("Location", backref="zone", lazy=True)
    modified = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
