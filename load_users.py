from db import db_session
from models import User
from users_list import users


def load_users(user_list, db_session):
    for user in user_list:
        user_for_add = User(name=user["email"], password=user["password"], status=user["status"])
        db_session.add(user_for_add)
    db_session.commit()


if __name__ == "__main__":
    load_users(user_list=users, db_session=db_session)
