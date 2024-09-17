FROM python:3.8-slim

COPY . /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable for port
ENV WEBSITED_PORT=80

# Expose port 80 to the outside
EXPOSE 80

CMD ["python3", "flaskapp.py"]