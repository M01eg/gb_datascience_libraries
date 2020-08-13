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




"""
Задание 4

Создайте датафрейм authors_stat на основе информации из
authors_price. В датафрейме authors_stat должны быть
четыре столбца:

author_name, min_price, max_price и mean_price,

в которых должны содержаться соответственно имя автора,
минимальная, максимальная и средняя цена на книги этого
автора.
"""

authors_min_price  = authors_price.groupby('author_name').agg({'price': 'min'})
authors_max_price  = authors_price.groupby('author_name').agg({'price': 'max'})
authors_mean_price = authors_price.groupby('author_name').agg({'price': 'mean'})

authors_stat = pd.merge(pd.merge(authors_min_price.rename(columns={'price': 'min_price'}),
                                 authors_max_price.rename(columns={'price': 'max_price'}),
                                 on='author_name'),
                        authors_mean_price.rename(columns={'price': 'mean_price'}),
                        on='author_name')

print(authors_stat)
print("\n")
