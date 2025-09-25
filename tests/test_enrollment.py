import pytest
from app import models, crud

def test_enroll_capacity(db_session):
    teacher = models.Teacher(name="Mr. X", subject="Math")
    course = models.Course(title="Algebra", capacity=1, teacher=teacher)
    student1 = models.Student(name="Alice")
    student2 = models.Student(name="Bob")
    db_session.add_all([teacher, course, student1, student2])
    db_session.commit()

    crud.enroll_student(db_session, student1.id, course.id)

    with pytest.raises(ValueError, match="Course capacity reached"):
        crud.enroll_student(db_session, student2.id, course.id)

def test_duplicate_enrollment(db_session):
    teacher = models.Teacher(name="Mr. Y", subject="Science")
    course = models.Course(title="Physics", capacity=2, teacher=teacher)
    student = models.Student(name="Charlie")
    db_session.add_all([teacher, course, student])
    db_session.commit()

    crud.enroll_student(db_session, student.id, course.id)

    with pytest.raises(ValueError, match="Duplicate enrollment"):
        crud.enroll_student(db_session, student.id, course.id)
