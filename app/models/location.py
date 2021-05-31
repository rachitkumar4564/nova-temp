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
    modified: str
    created: str
    __tablename__ = "location"
    __table_args__ = {"extend_existing": True}
    # id = db.Column(db.Integer, primary_key=True)
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(60), unique=True, nullable=True)
    longitude = db.Column(db.Numeric, nullable=True)
    latitude = db.Column(db.Numeric, nullable=True)
    full_address = db.Column(db.String, nullable=True)
    modified = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow())
    zone_locations = db.relationship(
        "ZoneLocation", backref=db.backref("location"), lazy=True
    )


@dataclass
class Zone(db.Model):
    id: UUID(as_uuid=True)
    name: str
    wave_points: str
    modified: str
    created: str
    __tablename__ = "zone"
    # __table_args__ = {"extend_existing": True}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = db.Column(db.String(60), unique=True, nullable=True)
    wave_points = db.Column(db.String(60), unique=True, nullable=True)
    modified = db.Column(
        db.String,
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    created = db.Column(db.String, nullable=False, default=datetime.datetime.utcnow)
    zone_locations = db.relationship(
        "ZoneLocation", backref=db.backref("zone"), lazy=True
    )


@dataclass
class ZoneLocation(db.Model):
    __tablename__ = "zonelocation"
    # __table_args__ = {"extend_existing": True}
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    zone_id = db.Column(UUID(as_uuid=True), db.ForeignKey("zone.id"))
    location_id = db.Column(UUID(as_uuid=True), db.ForeignKey("location.id"))
    modified = db.Column(
        db.String,
        nullable=False,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
    )
    created = db.Column(db.String, nullable=False, default=datetime.datetime.utcnow)

    # zone = db.relationship('Zone', backref='zone_location', lazy=True)
    # location = db.relationship('Location', backref='zonelocation', lazy=True)
