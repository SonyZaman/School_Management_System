---

# 📘 School Management System (SMS) + Scraper

A backend project built with **FastAPI** and **SQLAlchemy**, combined with a **web scraper** to demonstrate OOP concepts, CRUD operations, and business logic.

---

## 🚀 Features

### 🔹 Scraper
* Scrapes book data from **books.toscrape.com**
* Extracts: `title`, `url`, `category`, and `price/author`
* Saves scraped data into:
  * JSON file → `samples/scraped.json`
  * Database table → `scraped_resources`
* CLI support:
  ```bash
  python scraper/scrape.py --pages 3 --db
  ```

### 🔹 School Management System
* Built with **FastAPI** + **SQLAlchemy ORM**
* Domain models:
  * `Person` (abstract)
  * `Student`, `Teacher` (inheritance)
  * `Course` and `Enrollment` (many-to-many)
* **Business rules**:
  * Prevent duplicate enrollment
  * Enforce course capacity
* CRUD API endpoints for: Students, Teachers, Courses, Enrollments, and Scraped Resources

---

## ⚙️ Tech Stack

* **Backend**: FastAPI
* **ORM**: SQLAlchemy
* **Database**: PostgreSQL (can run with SQLite for testing)
* **Scraping**: Requests + BeautifulSoup
* **Testing**: Pytest
* **Migrations**: Alembic
* **Server**: Uvicorn

---

## 📂 Project Structure

```text
.
├── app/
│   ├── main.py          # FastAPI app with routes
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas (validation)
│   ├── crud.py          # CRUD functions
│   └── database.py      # DB connection/session
├── scraper/
│   └── scrape.py        # Scraper script
├── tests/               # Pytest test cases
├── samples/
│   └── scraped.json     # Sample scraped output
├── migrations/          # Alembic migrations
├── run.py               # Database initialization script
├── .env                 # DB connection config
├── requirements.txt     # Dependencies
└── README.md
```

---

## 📡 API Endpoints

### Students
* `POST /students` → Create student
* `GET /students/{id}` → Fetch student by ID
* `GET /students` → List all students

### Teachers
* `POST /teachers` → Create teacher
* `GET /teachers/{id}` → Fetch teacher by ID
* `GET /teachers` → List all teachers

### Courses
* `POST /courses` → Create course (with capacity)
* `GET /courses/{id}` → Fetch course by ID
* `GET /courses` → List all courses

### Enrollments
* `POST /students/{id}/enroll?course_id={course_id}` → Enroll student
  * ❌ Prevents duplicates
  * ❌ Checks capacity

### Scraped Resources
* `POST /import/scraped` → Import scraped JSON into DB
* `GET /scraped_resources` → List scraped resources

---

## 🛠️ Setup & Run

### 1️⃣ Clone the repo
```bash
git clone https://github.com/SonyZaman/School_Management_System.git
cd "school management system"
```

### 2️⃣ Create virtual environment & install deps
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
# venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 3️⃣ Set up environment variables (`.env`)
```env
DATABASE_URL=postgresql+psycopg2://postgres:yourpassword@localhost:5432/sms
```

### 4️⃣ Run database migrations/initialization
```bash
# Option 1: Using Alembic
alembic upgrade head

# Option 2: Using the initialization script
python run.py
```

### 5️⃣ Start FastAPI server
```bash
uvicorn app.main:app --reload
```

API will be available at: 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### 6️⃣ Run Scraper
```bash
python scraper/scrape.py --pages 2 --db
```

### 7️⃣ Run Tests
```bash
pytest -v
```

---

## ✅ Example Workflow

1. Create a teacher → `/teachers`
2. Create a course under that teacher → `/courses`
3. Create a student → `/students`
4. Enroll student in the course → `/students/{id}/enroll`
5. Scrape book data → `python scraper/scrape.py --pages 1 --db`
6. Fetch scraped data → `/scraped_resources`

---

## 🧩 OOP Pillars in the Project

* **Abstraction** → `Person` class is abstract
* **Inheritance** → `Student` and `Teacher` inherit from `Person`
* **Encapsulation** → Database session management in `database.py`
* **Polymorphism** → Students & Teachers behave differently when interacting with Courses

---

## 🧪 Tests Included

* Enrollment rules (capacity, duplicate prevention)
* API endpoint tests (student, teacher, course creation)
* Scraper parsing test

---

## 👨‍💻 Author

**SonyZaman** -- Python Intern Assignment
