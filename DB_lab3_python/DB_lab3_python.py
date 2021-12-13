from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables.Team import Team

from db.DBSession import DBSession

from DatabaseModel import DatabaseModel

from tables.Employee import Employee

def get_teams(session: DBSession) -> Team:
    team = session.query(Team).all()
    #print(f"ID: {employee.id}, {employee.first_name} {employee.last_name}")

    return team

model = DatabaseModel()

model.updateData()

