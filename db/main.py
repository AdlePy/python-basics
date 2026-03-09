from sqlmodel import Field, SQLModel, create_engine, Session, select


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    is_staff: bool | None = Field(default=False, nullable=False)


DATABASE_URL = "postgresql://postgres:777adlet@localhost:5432/blog"

engine = create_engine(DATABASE_URL, echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_users():
    user_1 = User(username="Askar Adilet", is_staff=True)
    user_2 = User(username="Askar Alisher")
    user_3 = User(username="Askar Altair")

    with Session(engine) as session:
        session.add(user_1)
        session.add(user_2)
        session.add(user_3)

        session.commit()


def select_users():
    with Session(engine) as session:
        statement = select(User)
        results = session.exec(statement)

        for user in results:
            print(user)


def select_user_by_id():
    with Session(engine) as session:
        statement = select(User).where(User.id == 1)
        results = session.exec(statement)
        user = results.one()
        print(user)


if __name__ == "__main__":
    # create_db_and_tables()
    # create_users()
    select_users()
    select_user_by_id()
