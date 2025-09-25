from sqlalchemy.orm import Session
from . import models, schemas

# ------------------ STUDENT ------------------

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(
        name=student.name,
        age=student.age,
        email=student.email
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def list_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


# ------------------ TEACHER ------------------

def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(
        name=teacher.name,
        subject=teacher.subject,
        email=teacher.email,
        phone=teacher.phone
    )
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def get_teacher(db: Session, teacher_id: int):
    return db.query(models.Teacher).filter(models.Teacher.id == teacher_id).first()

def list_teachers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Teacher).offset(skip).limit(limit).all()


# ------------------ COURSE ------------------

def create_course(db: Session, course: schemas.CourseCreate):
    db_course = models.Course(
        title=course.title,
        description=course.description,
        capacity=course.capacity,
        teacher_id=course.teacher_id
    )
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

def get_course(db: Session, course_id: int):
    return db.query(models.Course).filter(models.Course.id == course_id).first()

def list_courses(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Course).offset(skip).limit(limit).all()


# ------------------ ENROLLMENT ------------------

def enroll_student(db: Session, student_id: int, course_id: int):
    student = db.query(models.Student).get(student_id)
    course = db.query(models.Course).get(course_id)

    if not student or not course:
        raise ValueError("Student or Course not found")
    if student in course.students:
        raise ValueError("Duplicate enrollment")
    if len(course.students) >= course.capacity:
        raise ValueError("Course capacity reached")

    course.students.append(student)
    db.commit()
    db.refresh(course)
    return course


# ------------------ SCRAPED RESOURCES ------------------

def import_scraped(db: Session, resources: list[schemas.ScrapedResourceCreate]):
    objs = [models.ScrapedResource(**res.dict()) for res in resources]
    db.add_all(objs)
    db.commit()
    return objs

def list_scraped_resources(db: Session, category: str = None):
    query = db.query(models.ScrapedResource)
    if category:
        query = query.filter(models.ScrapedResource.category == category)
    return query.all()
