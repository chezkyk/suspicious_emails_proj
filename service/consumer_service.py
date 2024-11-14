from sqlalchemy.exc import SQLAlchemyError

from database.PostgreSQL_connection import session_maker
from models import User, Location, DeviceInfo, ExplosiveSentence, HostageSentence


def create_user(user_data):
    return User(
        username=user_data['username'],
        email=user_data['email']
    )

def create_location(location_data, user):
    return Location(
        latitude=location_data['latitude'],
        longitude=location_data['longitude'],
        city=location_data['city'],
        country=location_data['country'],
        user=user
    )

def create_device_info(device_data, user):
    return DeviceInfo(
        browser=device_data['browser'],
        os=device_data['os'],
        device_id=device_data['device_id'],
        user=user
    )

def process_sentences(sentences, user):
    for i, sentence in enumerate(sentences):
        if 'explosives' in sentence:
            explosive_sentence = ExplosiveSentence(sentence=sentence, user=user)
            user.explosive_sentences.append(explosive_sentence)

            for next_sentence in sentences[i + 1:i + 3]:
                user.explosive_sentences.append(ExplosiveSentence(sentence=next_sentence, user=user))

        elif 'hostage' in sentence:
            hostage_sentence = HostageSentence(sentence=sentence, user=user)
            user.hostage_sentences.append(hostage_sentence)

            for next_sentence in sentences[i + 1:i + 3]:
                user.hostage_sentences.append(HostageSentence(sentence=next_sentence, user=user))


def save_user_to_db(session, user):
    try:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user.id
    except SQLAlchemyError as e:
        session.rollback()
        print(f"error: {e}")
        raise
def insert_message(user_data):
    with session_maker() as session:
        user = create_user(user_data)

        location = create_location(user_data['location'], user)
        user.location = location

        device_info = create_device_info(user_data['device_info'], user)
        user.device_info = device_info

        if sentences := user_data.get('sentences', []):
            process_sentences(sentences, user)

        return save_user_to_db(session, user)