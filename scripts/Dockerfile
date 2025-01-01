# Use the official Python slim image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /scripts

# Copy the requirements file
COPY ./requirements.txt .

# Install required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy all scripts into the container
COPY ./* /scripts

# Command to run the Python server
CMD ["python3", "predict.py"]
