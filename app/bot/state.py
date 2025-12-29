from enum import Enum

class ChatState(Enum):
    NEW = "new"
    MENU = "menu"
    ASK_NAME = "ask_name"
    ASK_SERVICE = "ask_service"
    ASK_DATE = "ask_date"
    ASK_TIME = "ask_time"
    WAITING_HUMAN = "waiting_human"
    CLOSED = "closed"