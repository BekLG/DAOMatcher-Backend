from datetime import datetime, timezone, timedelta
from decouple import config
from random import choice
from string import ascii_letters, digits

import jwt

from src.controllers.user import get_user_by_id
from src.globals import USERS, Sessions
from src.models.user import User


def generate_random_string(length=8):
    characters = ascii_letters + digits
    return "".join(choice(characters) for _ in range(length))


def generate_access_token(userId: str):
    return jwt.encode(
        {
            "user_id": userId,
            "exp": datetime.now(timezone.utc)
            + timedelta(seconds=int(config("ACCESS_TOKEN_EXPIRY_IN_SECONDS"))),
        },
        config("SECRET_KEY"),
        algorithm="HS256",
    )


def generate_refresh_token(userId: str):
    payload = {
        "sub": userId,
        "iat": datetime.now(timezone.utc),
        "exp": datetime.now(timezone.utc)
        + timedelta(days=float(config("REFRESH_TOKEN_EXPIRY_IN_DAYS"))),
    }
    return jwt.encode(payload, config("SECRET_KEY"), algorithm="HS256")


def set_user_session(user_id: str):
    user_session = USERS.get(user_id)
    scoreUsers = Sessions.get(user_id)

    print(
        "user_id: ",
        user_id,
        "\tuser_sessions: ",
        user_session,
        "\tscoreUser: ",
        scoreUsers,
    )
    print("==========================================================")
    print("USERS: ", USERS)
    print("Sessions: ", Sessions)
    print("==========================================================")

    if not all([user_session, scoreUsers]):
        print(f"\033[91;1mUser session not found.\033[0m\n")
        return False, None

    scoreUsers.user_session = user_session
    print(f"\033[92mSet Current User: {scoreUsers.user_session}\033[0m")
    return user_session != None, user_session


def validate_data(jsonRequest):
    query = jsonRequest.get("query")
    user_list = jsonRequest.get("user_list")
    user_limit = jsonRequest.get("user_limit")
    depth = jsonRequest.get("depth")

    return all([query, user_list, user_limit, depth])


def emitData(socket, event, data=None, room=None):
    if room is None:
        print(f"\033[91;1mRoom is not set.\033[0m\n")
        return
    socket.emit(event, data=data, room=room)


def get_user_from_token(token):
    data = jwt.decode(token, config("SECRET_KEY"), algorithms=["HS256"])
    current_user = get_user_by_id(data.get("user_id")).json.get("data")
    return current_user
