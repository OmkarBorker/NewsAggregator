# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /main

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the entire application directory into the container
COPY . .

# Expose the port that the Flask app listens on
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application when the container launches
CMD ["flask", "run"]
