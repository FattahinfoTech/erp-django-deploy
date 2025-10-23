# Use Python 3.12 slim
FROM python:3.12-slim

# Prevent Python from writing .pyc files and enable stdout/stderr logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Run Gunicorn
CMD ["gunicorn", "erp_system.wsgi:application", "--bind", "0.0.0.0:8000"]
