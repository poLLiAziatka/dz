from db_session import SqlAlchemyBase
import sqlalchemy as sa
from sqlalchemy import orm


class News(SqlAlchemyBase):
    __tablename__ = "news"
    news_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True, )
    news_title = sa.Column(sa.String, nullable=True)
    news_content = sa.Column(sa.String, nullable=True)
    created_date = sa.Column(sa.DATETIME, nullable=True)
    is_private = sa.Column(sa.BOOLEAN, nullable=True)
    is_published = sa.Column(sa.BOOLEAN, nullable=True)
    user_id = sa.Column(sa.Integer, sa.ForeignKey("users.user_id"))

    user = orm.relation('User')
    categories = orm.relation("Category",
                              secondary="association",
                              backref="news")