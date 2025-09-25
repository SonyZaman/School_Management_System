def test_create_student(client):
    response = client.post("/students", json={"name": "John", "age": 20, "email": "john@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert "id" in data

def test_create_teacher_and_course(client):
    teacher = client.post("/teachers", json={"name": "Prof. Smith", "subject": "History", "email": "smith@example.com"}).json()
    response = client.post("/courses", json={"title": "History 101", "capacity": 2, "teacher_id": teacher["id"]})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "History 101"
    assert data["teacher_id"] == teacher["id"]

def test_enroll_student_api(client):
    student = client.post("/students", json={"name": "Jane", "email": "jane@example.com"}).json()
    teacher = client.post("/teachers", json={"name": "Dr. T", "subject": "Biology"}).json()
    course = client.post("/courses", json={"title": "Biology Basics", "capacity": 1, "teacher_id": teacher["id"]}).json()

    resp = client.post(f"/students/{student['id']}/enroll?course_id={course['id']}")
    assert resp.status_code == 200

    # second enrollment should fail (capacity reached)
    student2 = client.post("/students", json={"name": "Sam"}).json()
    resp2 = client.post(f"/students/{student2['id']}/enroll?course_id={course['id']}")
    assert resp2.status_code == 400
