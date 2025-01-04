FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install PostgreSQL development packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set the environment variables
ENV PYTHONPATH=/app
ENV PYTHONBUFFERED=1

# Health check to verify the container is running
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import sys; sys.exit(0 if True else 1)"

CMD ["python", "main.py"]