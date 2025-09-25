import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from app.database import Base, get_db
from fastapi.testclient import TestClient
from app.main import app


# Ensure project root in sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# SQLite in-memory DB with StaticPool (shared across connections)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Override FastAPI dependency
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# Run before each test
@pytest.fixture(autouse=True, scope="function")
def setup_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

# Fixture for API client
@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c

# Fixture for direct DB session (used in test_enrollment)
@pytest.fixture(scope="function")
def db_session():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
