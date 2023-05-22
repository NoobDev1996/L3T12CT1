# Use a Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the 'en_core_web_md' model
RUN python -m spacy download en_core_web_md

# Copy the solution files to the working directory
COPY . .

# Specify the command to run when the container starts
CMD ["python", "semantic.py"]

