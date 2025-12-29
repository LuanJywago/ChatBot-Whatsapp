from datetime import datetime, timedelta
from app.bot.state import ChatState

SESSIONS = {}

TIMEOUT_MINUTES = 30


def get_session(phone):
    session = SESSIONS.get(phone)

    if session:
        last = session["last_interaction"]
        if datetime.now() - last > timedelta(minutes=TIMEOUT_MINUTES):
            close_session(phone)
            return None

    return session


def create_session(phone):
    session = {
        "state": ChatState.MENU,
        "data": {},
        "last_interaction": datetime.now()
    }
    SESSIONS[phone] = session
    return session


def update_session(phone, state=None, data=None):
    session = SESSIONS.get(phone)
    if not session:
        return

    if state:
        session["state"] = state
    if data:
        session["data"].update(data)

    session["last_interaction"] = datetime.now()


def close_session(phone):
    if phone in SESSIONS:
        del SESSIONS[phone]
