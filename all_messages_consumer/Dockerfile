FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY all_messages_consumer.py .
CMD ["python", "all_messages_consumer.py"]