from yield_user import yield_user


if __name__ == "__main__":
    a = yield_user()
    b = next(a)
    print(f"Имя: {b.name} Статус: {b.status}")
