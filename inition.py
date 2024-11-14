from database.PostgreSQL_connection import session_maker
from models import User, DeviceInfo, Location, HostageSentence, ExplosiveSentence

def init():
    with session_maker() as session:

        user1 = User(username="user1", email="1@aa.com")
        user2 = User(username="user2", email="2@bb.com")


        device_info1 = DeviceInfo(device_id="device123", os="Android", browser="Chrome", user=user1)
        device_info2 = DeviceInfo(device_id="device456", os="iOS", browser="Safari", user=user2)

        location1 = Location(latitude=33.3333, longitude=34.3434, city="Tel Aviv", country="Israel", user=user1)
        location2 = Location(latitude=44.4444, longitude=-74.7474, city="Bney Brak", country="Israel", user=user2)

        hostage_sentence1 = HostageSentence(sentence="Ensure the hostage is kept in a soundproof room to avoid detection.", user=user1)
        hostage_sentence2 = HostageSentence(sentence="Keep the hostage under constant surveillance to prevent escape.", user=user2)

        explosive_sentence1 = ExplosiveSentence(sentence="The explosion will start the chain reaction. Make sure no one is nearby.", user=user1)
        explosive_sentence2 = ExplosiveSentence(sentence="Check that all explosives are armed before leaving the site.", user=user2)

        session.add_all(
            [user1, user2, device_info1, device_info2, location1, location2, hostage_sentence1, hostage_sentence2,
             explosive_sentence1, explosive_sentence2])

        session.commit()
    print("Data initialized successfully!")