# services/weather/src/api/models.py
""" Station model."""

# sqlalchemy
from sqlalchemy.sql import func
# instance db
from src import db

class Station(db.Model):
    """Station model."""
    __tablename__ = 'station'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(120), nullable=False)
    latitude =  db.Column(db.Float(), nullable=True)
    longitude =  db.Column(db.Float(), nullable=True)
    description = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    station_status = db.Column(db.Boolean(), default=True, nullable=False)
    current_condition = db.relationship('CurrentCondition')

class CurrentCondition(db.Model):
    """CurrentCondition model.
    """
    __tablename__ = 'current_condition'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    temperature = db.Column(db.Float(), nullable=False)
    humidity = db.Column(db.Float(), nullable=False)
    pm = db.Column(db.Float(),nullable=False )
    created_at = db.Column(db.DateTime, default=func.now(), nullable=False)
    station = db.Column(db.Integer, db.ForeignKey('station.id'))

    def __init__(self, temperature, humidity,pm,station):
        self.temperature = temperature
        self.humidity = humidity
        self.pm = pm
        self.station = station


    def to_json(self):
        return {
            'temperature': self.temperature,
            'humidity': self.humidity,
            'pm2': self.pm,
            'date': self.created_at
        }
