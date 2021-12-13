import timeit

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tables.Team import Team
from tables.Development import Development
from tables.Buyer import Buyer
from tables.Project import Project
from tables.ProjectOrder import ProjectOrder
from tables.Position import Position
from tables.Employee import Employee
from tables.base import BaseModel
from db.DBSession import DBSession

from sqlalchemy.inspection import inspect
from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import update
from sqlalchemy import desc
from sqlalchemy import func

class DatabaseModel(object):
    session: DBSession
    inspect_:None
    engine:None
    session_factory:None

    tableIndex = -1
    typeIndex = 0

    TYPES = {
        'Employee' : Employee,
        'Project' : Project,
        'ProjectOrder' : ProjectOrder,
        'Buyer' : Buyer,
        'Development' : Development,
        'Team' : Team,
        'Position' : Position,
    }

    def __init__(self):
        self.engine = create_engine(
        f'postgresql://postgres:reussite54321@localhost:5432/IT-company',
        pool_pre_ping=True
        )
        self.session_factory = sessionmaker(bind=self.engine)
        self.session = DBSession(self.session_factory())
        self.session.query(Team).all()

    def tablesBD(self):
        tables = inspect(self.engine).get_table_names()
        return tables

    def columns(self,table: str):
        inspect_mapper = inspect(self.TYPES[table])
        return inspect_mapper.columns.keys()

    def types(self,model: str):
        d = []
        table = self.TYPES[model]
        for c in table.__table__.columns:
            d.append(str(c.type))
        return d

    def primaryKey(self,table: str):
        inspect_mapper = inspect(self.TYPES[table])
        return inspect_mapper.primary_key[0].name

    def insertData(self):
        tables = self.tablesBD()
        print('Choose table:')
        tableIndex = 1
        for table in tables:
            print(tableIndex,table)
            tableIndex = tableIndex + 1
        tableIndex = int(input())
        #print('table: ',tables[tableIndex - 1])
        cols = self.columns(tables[tableIndex - 1])
        types = self.types(tables[tableIndex - 1])
        data = {}
        typeIndex = 0
        for col in cols:
            print('Insert value for column ',col)
            strType = types[typeIndex]
            val = type(strType)(input())
            typeIndex = typeIndex + 1
            data[col] = val
        emp = self.TYPES[tables[tableIndex - 1]](**data)
        self.session._session.add(emp)  
        self.session._session.commit()

    def deleteData(self):

        tables = self.tablesBD()
        print('Choose table:')
        tableIndex = 1

        for table in tables:
            print(tableIndex,table)
            tableIndex = tableIndex + 1
        tableIndex = int(input())

        print("Choose the value for column id")

        types = self.types(tables[tableIndex - 1])
        cols = self.columns(tables[tableIndex - 1])
        #print(types[cols.index(primary)].type)

        val = int(input())
        self.session._session.query(self.TYPES[tables[tableIndex - 1]]).filter(self.TYPES[tables[tableIndex - 1]].id == val).delete()
        self.session._session.commit()

    def updateData(self):
        tables = self.tablesBD()
        print('Choose table:')
        tableIndex = 1
        for table in tables:
            print(tableIndex,table)
            tableIndex = tableIndex + 1
        tableIndex = int(input())
        tableIndex = tableIndex - 1

        print("Choose the value for column id")

        types = self.types(tables[tableIndex])
        cols = self.columns(tables[tableIndex])
 
        val = int(input())
        table = self.TYPES[tables[tableIndex]]
        data = {}
        typesIndex = 0
        for col in cols:
            strtype = types[typesIndex]
            typesIndex = typesIndex + 1
            print('Want to update column ',col,'? y/n')
            choose = str(input())
            if choose == 'y':
                print('Input value for column ',col)
                colValue = type(strtype)(input())
                data[col] = colValue
        item = self.session._session.query(table).filter(table.id == val).one()
        for key in data:
            setattr(item,key,data[key])
        self.session._session.commit()

    def select_teams(self):
        self.engine.execute("SELECT * FROM \"Team\"")


            