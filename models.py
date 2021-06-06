from sqlalchemy import Column, Integer, String
from db import Base, engine


class User(Base):
    __tablename__ = 'users_list'
    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    password = Column(String)
    status = Column(String)

    def __repr__(self):
        return f'<User {self.name} , status = {self.status}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
