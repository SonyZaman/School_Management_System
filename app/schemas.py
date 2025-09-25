#data transfer class

from pydantic import BaseModel
from typing import List, Optional

class StudentBase(BaseModel):
    name: str
    age: Optional[int] = None
    email: Optional[str] = None

class StudentCreate(StudentBase): pass

class Student(StudentBase):
    id: int
    class Config: orm_mode = True


class TeacherBase(BaseModel):
    name: str
    subject: str
    email: Optional[str] = None
    phone: Optional[str] = None

class TeacherCreate(TeacherBase): pass

class Teacher(TeacherBase):
    id: int
    class Config: orm_mode = True


class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    capacity: int
    teacher_id: int

class CourseCreate(CourseBase): pass

class Course(CourseBase):
    id: int
    students: List[Student] = []
    class Config: orm_mode = True


class ScrapedResourceBase(BaseModel):
    title: str
    url: str
    category: str
    price_or_author: str

class ScrapedResourceCreate(ScrapedResourceBase): pass

class ScrapedResource(ScrapedResourceBase):
    id: int
    class Config: orm_mode = True
