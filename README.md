# School Management System (FastAPI)

A comprehensive FastAPI-based School Management System for managing students, teachers, courses, and enrollments. It also includes features for managing scraped educational resources.

## 🚀 Features

- **🎓 Student Management**: CRUD operations for students (Name, Age, Email).
- **👨‍🏫 Teacher Management**: CRUD operations for teachers (Name, Subject, Email, Phone).
- **📚 Course Management**: Create and list courses with capacity and teacher assignment.
- **📝 Enrollment System**: Enroll students into courses with capacity validation.
- **🔍 Scraped Resources**: Import and manage educational resources scraped from external sources.
- **🛠️ Database**: Powered by PostgreSQL and SQLAlchemy ORM.
- **📜 Documentation**: Auto-generated Swagger (OpenAPI) and ReDoc documentation.

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Server**: Uvicorn

## 📋 Project Structure

```text
.
├── app/
│   ├── main.py          # Entry point and API routes
│   ├── models.py        # Database models (SQLAlchemy)
│   ├── schemas.py       # Pydantic models for validation
│   ├── crud.py          # Database logic (Create, Read, Update, Delete)
│   └── database.py      # Database connection setup
├── run.py               # Script for initializing database tables
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (DB URL)
└── venv/                # Virtual environment
```

## ⚙️ Setup & Installation

### 1. Prerequisites
- Python 3.8+
- PostgreSQL installed and running

### 2. Clone the Project
```bash
git clone <repository-url>
cd "school management system"
```

### 3. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On MacOS/Linux
# Or on Windows: venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables
Create a `.env` file in the root directory (if not exists) and add your PostgreSQL connection string:
```env
DATABASE_URL=postgresql+psycopg2://<username>:<password>@localhost:5432/<database_name>
```

### 6. Initialize Database
Run the following script to create the necessary tables in your PostgreSQL database:
```bash
python run.py
```

##  Running the Application

Start the FastAPI server using Uvicorn:
```bash
uvicorn app.main:app --reload
```



## 📡 Key Endpoints

- `POST /students` - Create a new student
- `GET /students` - List all students
- `POST /teachers` - Create a new teacher
- `POST /courses` - Create a new course
- `POST /students/{id}/enroll` - Enroll a student in a course
- `GET /scraped_resources` - View imported educational resources
