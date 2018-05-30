# http://peewee.readthedocs.io/en/latest/index.html

import peewee
from peewee import *

db = MySQLDatabase('guest_book', user='root', passwd='')

class Book(peewee.Model):
    author = peewee.CharField()
    title = peewee.TextField()

    class Meta:
        database = db

Book.create_table()
book = Book(author="me", title='Peewee is cool')
book.save()
for book in Book.filter(author="me"):
    print(book.title)