FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY explosiv_messages_consumer.py .
CMD ["python", "explosiv_messages_consumer.py"]