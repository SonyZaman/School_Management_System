from app.database import Base, engine
from app import models

print("⏳ Creating tables in PostgreSQL...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")
