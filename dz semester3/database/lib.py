import sqlite3

conn = sqlite3.connect("C:\ProgramPoli\SQLiteStudio-3.2.1\lib")
cursor = conn.cursor()

cursor.execute("""INSERT INTO Library VALUES (1, 'Ленина 666', '267-2021')""")
cursor.execute("""INSERT INTO Library VALUES (2, 'Эволюционный Тупик 77', '3-3:10')""")
cursor.execute("""INSERT INTO Library VALUES (3, 'Пустая 1', '24ч')""")

cursor.execute("""INSERT INTO Book VALUES (1, 'Лучший УИР за всю историю вселенной', 'Азиатцева П.В. и Белоусова 
У.М', 1)""")
cursor.execute("""INSERT INTO Book VALUES (2, 'Как законить лицей и не сойти с ума', 'Неизвестный А.Б', 2)""")
cursor.execute("""INSERT INTO Book VALUES (3, 'Политех или Мак: что делать если не сдал егэ', 'Неизвестный А.Б', 
3)""")

cursor.execute("""INSERT INTO Reader VALUES (1, 'Иванов И.И', '88005553535', 1)""")
cursor.execute("""INSERT INTO Reader VALUES (2, 'Иванов В.И', '88002002316', 2)""")
cursor.execute("""INSERT INTO Reader VALUES (3, 'Иванов С.И', '2014461', 3)""")

cursor.execute("""INSERT INTO Employee VALUES (1, 'Иванов И.В', 1, 'Библиотекарь' )""")
cursor.execute("""INSERT INTO Employee VALUES (2, 'Иванова М.Ж', 1, 'Охранник' )""")
cursor.execute("""INSERT INTO Employee VALUES (3, 'Сидоров К.К.', 2, 'Директор' )""")

cursor.execute("""INSERT INTO Book_in_lib VALUES (1, 1)""")
cursor.execute("""INSERT INTO Book_in_lib VALUES (1, 2)""")
cursor.execute("""INSERT INTO Book_in_lib VALUES (2, 3)""")

cursor.execute("""INSERT INTO Reader_in_lib VALUES (1, 3)""")
cursor.execute("""INSERT INTO Reader_in_lib VALUES (2, 2)""")
cursor.execute("""INSERT INTO Reader_in_lib VALUES (3, 1)""")

conn.commit()

