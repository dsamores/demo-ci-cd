FROM python:3.9-slim

# Working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY app/requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY ./app /app

# Expose the server port
EXPOSE 8080

# Command to start the server
# CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
CMD ["python", "app.py"]
