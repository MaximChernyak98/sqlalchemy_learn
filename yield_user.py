from models import User
import random


def yield_user():
    rowCount = int(User.query.count())
    print(f"Запустил шилд дженерейтор")
    for i in range(6):
        my_user = User.query.offset(int(rowCount*random.random())).first()
        print(f"Выдал один раз Имя: {my_user.name} Статус: {my_user.status}")
        yield my_user
