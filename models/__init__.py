from sqlalchemy.orm import declarative_base

Base = declarative_base()

from .user import User
from .location import Location
from .device_info import DeviceInfo
from .hostage_sentence import HostageSentence
from .explosiv_sentence import ExplosiveSentence