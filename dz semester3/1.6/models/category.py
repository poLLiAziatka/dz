from db_session import SqlAlchemyBase
import sqlalchemy as sa
from sqlalchemy import orm

association_table = sa.Table('association', SqlAlchemyBase.metadata,
                             sa.Column('news', sa.Integer, sa.ForeignKey('news.news_id')),
                             sa.Column('category', sa.Integer, sa.ForeignKey('category.category_id')))


class Category(SqlAlchemyBase):
    __tablename__ = "category"
    category_id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    name = sa.Column(sa.String, nullable=True)


