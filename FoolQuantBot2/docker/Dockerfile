# FoolQuantBot Dockerfile
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy bot source code
COPY bot/ /app/bot/
COPY config/ /app/config/
COPY scripts/ /app/scripts/

# Install dependencies
RUN pip install -r /app/scripts/requirements.txt

# Set entrypoint
CMD ["python", "/app/bot/core/multi_exchange_executor.py"]
