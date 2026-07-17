# Start from an official Python image (our base environment)
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy requirements first, then install (this layer gets cached)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code and model files in
COPY . .

# Document the port the app uses
EXPOSE 8000

# The command that runs when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]