import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_message(email):
    email = {
        "email": email.get("email"),
        "username": email.get("username"),
        "ip_address": email.get("ip_address"),
        "created_at": email.get("created_at"),
        "location": {
            "latitude": email.get("latitude"),
            "longitude": email.get("longitude"),
            "city": email.get("city"),
            "country": email.get("country"),
        },
        "device_info": {
            "browser": email.get("browser"),
            "os": email.get("os"),
            "device_id": email.get("device_id"),
        },
        "sentences": email.get("sentences"),
    }
    producer.send('messages.all', value=email)
def reverse_sentences(email):
    suspicious_keywords = ["explosives", "hostage"]
    reordered_sentences = sorted(
        email.get('sentences', []),
        key=lambda sentence: any(keyword in sentence for keyword in suspicious_keywords),
        reverse=True
    )
    email['sentences'] = reordered_sentences

def check_suspicious_word(email):
    for sentence in email.get('sentences', []):
        if "explosives" in sentence:
            reverse_sentences(email)
            producer.send('messages.explosive',value=email)
            return
        elif "hostage" in sentence:
            reverse_sentences(email)
            producer.send('messages.hostage',value=email)
            return
