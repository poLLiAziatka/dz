from db_session import SqlAlchemyBase
import sqlalchemy as sa
from sqlalchemy import orm


class User(SqlAlchemyBase):
    __tablename__ = "users"
    user_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String)
    email = sa.Column(sa.String, unique=True)

    news = orm.relation("News", back_populates='user')