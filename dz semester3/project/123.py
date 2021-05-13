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
conn = sqlite3.connect("C://Users//Polina//PycharmProjects//dz semester3//project//db_fact")
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
def create_new_subcat(subcategory, category, col):
    cursor.execute(f'''INSERT INTO categories (category, subcategory) VALUES({category}, {subcategory})''')
    cursor.execute(
        f'''CREATE TABLE {subcategory} (id SMALLINT NOT NULL PRIMARY KEY, {[f'{i} VARCHAR,' for i in col]})''')
    conn.commit()


# добавление фактов
def add_facts(subcategory, col, fact):
    cursor = conn.execute(f'select * from {subcategory}')
    names = list(map(lambda x: x[0], cursor.description))
    cursor = conn.cursor()
    for i in range(len(col)):
        if col[i] not in names:
            cursor.execute(f'''ALTER TABLE {subcategory} ADD COLUMN "{col[i]}" CHAR''')
        cursor.execute(f'''INSERT INTO {subcategory} ('{col[i]}') VALUES('{fact[i]}''')
    conn.commit()


# вот это надо взять из ввода(поиск конкретного факта)
request = "Первая мировая война"


class QuotesSpider(scrapy.Spider):
    name = "wiki"
    start_urls = [
        f'https://ru.wikipedia.org/wiki/{request}']

    def parse(self, response):
        th = response.xpath('//th[has-class("plainlist")]/text()').extract()
        td = response.xpath('//td[has-class("plainlist")]/text()').extract()
        th.insert(0, "main")
        td.insert(0, request)
        add_facts('Войны', th, td)



add_facts("'Войны'",
          ['main', 'Государство', 'Административно-территориальная единица', 'Дата начала', 'Дата окончания',
           'Участник(и)'],
          ["Война с эму", "Австралия", "Западная Австралия", "ноябрь 1932", "ноябрь 1932",
           "Джордж Пирс, эму и Силы обороны Австралии"])
