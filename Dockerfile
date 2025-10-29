FROM python:3.9-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .

# Create directory for SQLite database
RUN mkdir -p /app/data

EXPOSE 5000

CMD ["python", "app.py"]