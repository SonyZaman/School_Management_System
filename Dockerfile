# # Base image
# FROM python:3.10



# # Set working directory
# WORKDIR /app

# # Install system dependencies (psycopg2 এর জন্য)
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy project files
# COPY . .

# # Expose FastAPI port
# EXPOSE 8000

# # Run the FastAPI app with uvicorn
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

