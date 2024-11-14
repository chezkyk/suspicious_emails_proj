import json
from kafka import KafkaConsumer

from service.consumer_service import insert_message


consumer = KafkaConsumer(
    'messages.hostage',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='email_messages',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)


for msg in consumer:
    message = msg.value
    print(f"Received message: {message}")
    insert_message(message)
    print("Message inserted")
