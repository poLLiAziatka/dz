import scrapy
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper
import sqlite3

'''
engine = create_engine('sqlite:///db_fact', echo=True)

metadata = MetaData()
main_table = Table('categories', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('category', String),
                   Column('subcategory', String)
                   )

metadata.create_all(engine)

'''
conn = sqlite3.connect("C:/Users/Polina/PycharmProjects/dz semester3/project/db_fact")
cursor = conn.cursor()

'''
class Сategories(object):
    def __init__(self, category, subcategory):
        self.category = category
        self.subcategory = subcategory

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.category, self.subcategory)

    # mapper(Сategories, main_table)
'''


# создание новой таблицы подкатегории
def create_new_subcat(self, subcategory, category, *args):
    cursor.execute(f'''INSERT INTO categories () VALUES ({category}, {subcategory})''')
    cursor.execute(
        f'''CREATE TABLE {subcategory} (id SMALLINT NOT NULL PRIMARY KEY, {[f'{i} VARCHAR,' for i in args]})''')
    conn.commit()


# добавление фактов
def add_facts(subcategory, col, fact):
    cursor = conn.execute(f'select * from {subcategory}')
    names = list(map(lambda x: x[0], cursor.description))
    cursor = conn.cursor()
    for i in col:
        if i not in names:
            cursor.execute(f'''ALTER TABLE {subcategory} ADD COLUMN {i} CHAR''')
    cursor.execute(f'''INSERT INTO {subcategory} ({col}) VALUES({fact})''')


# вот это надо взять из ввода(поиск конкретного факта)
request = "Первая мировая война"


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        f'https://ru.wikipedia.org/wiki/{request}']

    def parse(self, response):
        th = response.xpath('//th[has-class("plainlist")]/text()').extract()
        td = response.xpath('//td[has-class("plainlist")]/text()').extract()
        th.insert(0, "main")
        td.insert(0, request)
        add_facts('Войны', th, td)

