# -*- coding: utf-8 -*-

"""
Задание 1

Импортируйте библиотеку Pandas и дайте ей псевдоним pd.
Создайте датафрейм authors со столбцами author_id и
author_name, в которых соответственно содержатся данные:
[1, 2, 3] и ['Тургенев', 'Чехов', 'Островский']. Затем
создайте датафрейм book cо столбцами author_id,
book_title и price, в которых соответственно содержатся
данные: 
[1, 1, 1, 2, 2, 3, 3], 
['Отцы и дети', 'Рудин', 'Дворянское гнездо', 'Толстый и тонкий',
 'Дама с собачкой', 'Гроза', 'Таланты и поклонники'],
[450, 300, 350, 500, 450, 370, 290].
"""

import pandas as pd

authors = pd.DataFrame({'author_id': [1, 2, 3],
                        'author_name': ['Тургенев', 'Чехов', 'Островский']})

books = pd.DataFrame({'author_id': [1, 1, 1, 2, 2, 3, 3],
                      'book_title': ['Отцы и дети', 'Рудин',
                                     'Дворянское гнездо','Толстый и тонкий',
                                     'Дама с собачкой', 'Гроза',
                                     'Таланты и поклонники'],
                      'price': [450, 300, 350, 500, 450, 370, 290]})

print(authors)
print("\n")
print(books)
print("\n")




"""
Задание 2

Получите датафрейм authors_price, соединив датафреймы
authors и books по полю author_id.
"""

authors_price = pd.merge(authors, books, on='author_id')
print(authors_price)
print("\n")




"""
Задание 3

Создайте датафрейм top5, в котором содержатся строки
из authors_price с пятью самыми дорогими книгами.
"""


top5 = authors_price.sort_values('price', ascending=False).head(5)
print(top5)
print("\n")



