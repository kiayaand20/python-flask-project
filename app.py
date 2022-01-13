from flask import Flask
from flask import request
from flask import jsonify

from peewee import *
from playhouse.shortcuts import model_to_dict

db = PostgresqlDatabase('memes', user='postgres',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Meme(BaseModel):
    name = CharField()
    url = CharField()
    width = CharField()
    height = CharField()
    box_count = CharField()


db.connect()
db.drop_tables([Meme])
db.create_tables([Meme])

meme1 = Meme(name='Drake Hotline Bling', url='https://i.imgflip.com/30b1gx.jpg',
             width='1200', height='1200', box_count='2')
meme1.save()

app = Flask(__name__)


@app.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "Hello GET"})
    else:
        return jsonify({"message": "Hello, world!"})


@app.route('/meme', methods=['GET'])
@app.route('/meme/<id>', methods=['GET'])
def meme(id=None):
    if id:
        meme = Meme.get(Meme.id == id)
        meme = model_to_dict(meme)
        return jsonify(meme)
    memes = []
    for meme in Meme.select():
        memes.append(model_to_dict(meme))
    return jsonify(memes)


@app.route('/name/<name>', methods=['GET'])
def name(name=None):
    if name:
        meme = Meme.get(Meme.name == name)
        meme = model_to_dict(meme)
        return jsonify(meme)
    memes = []
    for meme in Meme.select():
        memes.append(model_to_dict(meme))
    return jsonify(memes)


@app.route('/width/<width>', methods=['GET'])
def meme2(width=None):
    if width:
        meme = Meme.get(Meme.width == width)
        meme = model_to_dict(meme)
        return jsonify(meme)
    memes = []
    for meme in Meme.select():
        memes.append(model_to_dict(meme))
    return jsonify(memes)


app.run(port=9000, debug=True)
