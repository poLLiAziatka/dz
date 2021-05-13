from users import User
from news import News
import db_session
from category import Category

db_session.global_init()
session = db_session.create_session()

user_1 = User(name="Santa", email="DedMoros@mail.ru")
session.add(user_1)
session.commit()

user_2 = User(name='Putin', email='theief@gmail.ru')
session.add(user_2)
session.commit()

user_3 = User(name='Neo', email='the_closen_one@mail.ru')
session.add(user_3)
session.commit()

news1 = News(news_title="Tax", news_content="Have you paid taxes?")
news1.user_id = user_2.user_id
session.commit()

news2 = News(news_title="Present", news_content="If you misbehave, i will give you Covid-21")
news2.user_id = user_1.user_id
session.add(news2)
session.commit()

news3 = News(news_title="New Year's adddress from the president", news_content="I'm resetting 2020")
news3.user_id = user_2.user_id
session.add(news3)
session.commit()

news4 = News(news_title='1000101001', news_content="01010010010100010100")
news4.user_id = user_3.user_id
session.add(news4)
session.commit()

category1 = Category(name='Tragicomedy')
news1.categories.append(category1)
news4.categories.append(category1)
session.commit()

category2 = Category(name='Vaudeville')
news2.categories.append(category2)
session.commit()

category3 = Category(name='Farce')
news3.categories.append(category3)
session.commit()

