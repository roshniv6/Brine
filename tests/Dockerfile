# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the app directory into the container at /app
COPY ./Brine/app/ .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
ENV NAME World

# Run main.py when the container launches
CMD ["python", "main.py"]
