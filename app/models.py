#database table design

from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from .database import Base

# Association Table
enrollment_table = Table(
    "enrollments", Base.metadata,
    Column("student_id", ForeignKey("students.id"), primary_key=True),
    Column("course_id", ForeignKey("courses.id"), primary_key=True)
)

class ScrapedResource(Base):
    __tablename__ = "scraped_resources"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    url = Column(String)
    category = Column(String)
    price_or_author = Column(String)

class Person(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

class Student(Person):
    __tablename__ = "students"
    age = Column(Integer, nullable=True)
    email = Column(String, unique=True, nullable=True)
    courses = relationship("Course", secondary=enrollment_table, back_populates="students")

class Teacher(Person):
    __tablename__ = "teachers"
    subject = Column(String)
    email = Column(String, unique=True, nullable=True)
    phone = Column(String, nullable=True)

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String, nullable=True)   # new field
    capacity = Column(Integer)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))
    teacher = relationship("Teacher")
    students = relationship("Student", secondary=enrollment_table, back_populates="courses")
