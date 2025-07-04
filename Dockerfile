# Build on top of an official Python image
FROM python:3.11-alpine

# Set the working directory in the container to /app
WORKDIR /app

# This copies the requirements.txt and installs the dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copies the application code from the present directory into the container
COPY app.py /app/app.py

# Exposes port 8080 for the app
EXPOSE 8080

# Run the Flask app
CMD ["python", "app.py"]
