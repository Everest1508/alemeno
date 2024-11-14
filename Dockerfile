# Dockerfile

# Use the official Python image
FROM python:3.11

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy project files
COPY . /code/
