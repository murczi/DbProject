from Entities import Classes, MarkTypes, Weights, Subjects, Base, Students
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sqlite.db')

# Step 6: Create the tables in the database
Base.metadata.create_all(engine)

# Step 7: Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Step 8: Insert data into the table

classes = [Classes(Class="A"), Classes(Class="B"), Classes(Class="C"), Classes(Class="D"), Classes(Class="E")]
markTypes = [MarkTypes(Value=1), MarkTypes(Value=2), MarkTypes(Value=3), MarkTypes(Value=4), MarkTypes(Value=5)]
weights = [Weights(Value=1, Type="Oral Exam"), Weights(Value=2, Type="Written Exam"),
           Weights(Value=0.5, Type="Homework")]
subjects = [Subjects(Subject="Math"), Subjects(Subject="Physics"), Subjects(Subject="Chemistry"),
            Subjects(Subject="Programming"), Subjects(Subject="Biology")]
session.add_all(classes)
session.add_all(markTypes)
session.add_all(weights)
session.add_all(subjects)

# Commit the transaction
session.commit()

session.close()
