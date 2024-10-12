from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Students(Base):
    __tablename__ = 'Students'

    ID = Column(Integer, primary_key=True)
    Name = Column(String)
    ClassID = Column(Integer, ForeignKey('Classes.ID'))

    Class = relationship("Classes", back_populates="Students")
    Marks = relationship("Marks", back_populates="Student")

    def __repr__(self):
        return f"<Students(ID={self.ID}, Name={self.Name}, ClassID={self.ClassID})>"

class Marks(Base):
    __tablename__ = 'Marks'

    ID = Column(Integer, primary_key=True)
    StudentID = Column(Integer, ForeignKey('Students.ID'))
    MarkTypeID = Column(Integer, ForeignKey('MarkTypes.ID'))
    SubjectID = Column(Integer, ForeignKey('Subjects.ID'))
    WeightID = Column(Integer, ForeignKey('Weights.ID'))
    Date = Column(DateTime)

    Student = relationship("Students", back_populates="Marks")
    MarkType = relationship("MarkTypes", back_populates="Marks")
    Subjects = relationship("Subjects", back_populates="Marks")
    Weights = relationship("Weights", back_populates="Marks")

    def __repr__(self):
        return f"<Marks(ID={self.ID})>"


class Classes(Base):
    __tablename__ = 'Classes'

    ID = Column(Integer, primary_key=True)
    Class = Column(String)

    Students = relationship("Students", back_populates="Class")

    def __repr__(self):
        return f"<Classes(ID={self.ID}, Class={self.Class})>"


class MarkTypes(Base):
    __tablename__ = 'MarkTypes'

    ID = Column(Integer, primary_key=True)
    Value = Column(Integer)

    Marks = relationship("Marks", back_populates="MarkType")

    def __repr__(self):
        return f"<MarkTypes(ID={self.ID}, Value={self.Value})>"


class Subjects(Base):
    __tablename__ = 'Subjects'

    ID = Column(Integer, primary_key=True)
    Subject = Column(String)

    Marks = relationship("Marks", back_populates="Subjects")

    def __repr__(self):
        return f"<Subjects(ID={self.ID}, Subject={self.Subject})>"


class Weights(Base):
    __tablename__ = 'Weights'

    ID = Column(Integer, primary_key=True)
    Value = Column(Float)
    Type = Column(String)

    Marks = relationship("Marks", back_populates="Weights")

    def __repr__(self):
        return f"<Weights(ID={self.ID}, Value={self.Value})>"