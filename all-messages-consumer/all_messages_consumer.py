import json

from kafka import KafkaConsumer

from database.mongo_db_connection import get_mongo_connection
consumer = KafkaConsumer(
    'messages.all',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='email_messages',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for msg in consumer:
    message = msg.value
    db = get_mongo_connection()
    db.insert_one(message)
    print("message inserted")

