FROM 763104351884.dkr.ecr.eu-west-1.amazonaws.com/pytorch-inference:2.2.0-gpu-py310-cu118-ubuntu20.04-sagemaker

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code into the container
COPY . .

# Expose port 8080 to allow external access to the Flask application
EXPOSE 8080

# Define the entry point for running the Flask application
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]