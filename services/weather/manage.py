# services/weather/manage.py

from flask.cli import FlaskGroup

from src import create_app, db
from src.api.models import Station, CurrentCondition

app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    """Seeds the database"""
    db.session.add(Station(name='Santa lucia',latitude=10.398,longitude=-75.483,description='description'))
    db.session.add(CurrentCondition(temperature=25.8, humidity=58.3,pm=35,station=1))
    db.session.add(CurrentCondition(temperature=28.6, humidity=45.6,pm=55.5,station=1))
    db.session.commit()


if __name__ == '__main__':
    cli()
