# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . .

# Install any dependencies
RUN pip install locust

# Expose the Locust web UI port (default is 8089)
EXPOSE 8089

# Command to run Locust
CMD ["locust", "-f", "locustfile.py", "--host=https://php-app-mod-dev-399807308626.us-central1.run.app"]
