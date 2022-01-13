from peewee import *


db = PostgresqlDatabase(
    'memes', user='postgres', password='', host='localhost', port=5432)
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class Meme(BaseModel):
    name = CharField()
    url = CharField()
    width = CharField()
    height = CharField()
    box_count = CharField()


# kiaya = Person.get(Person.first_name == 'Kiaya')
# kiaya.delete_instance()

db.create_tables([Meme])

meme1 = Meme(name='Drake Hotline Bling', url='https://i.imgflip.com/30b1gx.jpg',
             width='1200', height='1200', box_count='2')
meme1.save()
