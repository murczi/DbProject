from Entities import Classes, MarkTypes, Weights, Subjects, Students, Marks
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlite.db')
Session = sessionmaker(bind=engine)
session = Session()

print(session.query(Classes).filter(Classes.Class == "E"))