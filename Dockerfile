# Use an official Python image as base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port the app runs on
EXPOSE 80

# Run the app
CMD ["python", "app.py"]
