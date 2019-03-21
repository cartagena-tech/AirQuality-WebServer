# services/weather/src/api/models.py
""" Station model."""

# sqlalchemy
from sqlalchemy.sql import func
# instance db
from src import db


class Station(db.Model):
    """Station model.
    """
    __tablename__ = 'stations'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    temperature = db.Column(db.Float(), nullable=False)
    humidity = db.Column(db.Float(), nullable=False)
    pm = db.Column(db.Float(),nullable=False )
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)

    def __init__(self, temperature, humidity,pm):
        self.temperature = temperature
        self.humidity = humidity
        self.pm = pm

    def to_json(self):
        return {
            'temperature': self.temperature,
            'humidity': self.humidity,
            'pm2': self.pm,
            #'active': self.active,
            'date': self.created_date
        }