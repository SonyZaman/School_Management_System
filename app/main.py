from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# ------------------ STUDENT ------------------

@app.post("/students", response_model=schemas.Student)
def create_student(student: schemas.StudentCreate, db: Session = Depends(database.get_db)):
    return crud.create_student(db, student)

@app.get("/students/{student_id}", response_model=schemas.Student)
def get_student(student_id: int, db: Session = Depends(database.get_db)):
    db_student = crud.get_student(db, student_id)
    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student

@app.get("/students", response_model=list[schemas.Student])
def list_students(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.list_students(db, skip=skip, limit=limit)


# ------------------ TEACHER ------------------

@app.post("/teachers", response_model=schemas.Teacher)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(database.get_db)):
    return crud.create_teacher(db, teacher)

@app.get("/teachers/{teacher_id}", response_model=schemas.Teacher)
def get_teacher(teacher_id: int, db: Session = Depends(database.get_db)):
    db_teacher = crud.get_teacher(db, teacher_id)
    if not db_teacher:
        raise HTTPException(status_code=404, detail="Teacher not found")
    return db_teacher

@app.get("/teachers", response_model=list[schemas.Teacher])
def list_teachers(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.list_teachers(db, skip=skip, limit=limit)


# ------------------ COURSE ------------------

@app.post("/courses", response_model=schemas.Course)
def create_course(course: schemas.CourseCreate, db: Session = Depends(database.get_db)):
    return crud.create_course(db, course)

@app.get("/courses/{course_id}", response_model=schemas.Course)
def get_course(course_id: int, db: Session = Depends(database.get_db)):
    db_course = crud.get_course(db, course_id)
    if not db_course:
        raise HTTPException(status_code=404, detail="Course not found")
    return db_course

@app.get("/courses", response_model=list[schemas.Course])
def list_courses(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.list_courses(db, skip=skip, limit=limit)


# ------------------ ENROLLMENT ------------------

@app.post("/students/{student_id}/enroll")
def enroll(student_id: int, course_id: int, db: Session = Depends(database.get_db)):
    try:
        return crud.enroll_student(db, student_id, course_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


# ------------------ SCRAPED RESOURCES ------------------

@app.post("/import/scraped", response_model=list[schemas.ScrapedResource])
def import_scraped(resources: list[schemas.ScrapedResourceCreate], db: Session = Depends(database.get_db)):
    return crud.import_scraped(db, resources)

@app.get("/scraped_resources", response_model=list[schemas.ScrapedResource])
def get_scraped(category: str = None, db: Session = Depends(database.get_db)):
    return crud.list_scraped_resources(db, category=category)
