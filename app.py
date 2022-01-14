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


class Memes(BaseModel):
    name = CharField()
    url = CharField()
    width = IntegerField()
    height = IntegerField()
    box_count = IntegerField()


db.connect()

app = Flask(__name__)


@app.route('/memes', methods=['GET'])
@app.route('/memes/<id>', methods=['GET'])
def meme(id=None):
    if id:
        meme = Memes.get(Memes.id == id)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/memes/name/<name>', methods=['GET'])
def name(name=None):
    if name:
        meme = Memes.get(Memes.name == name)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/memes/width/<width>', methods=['GET'])
def width(width=None):
    if width:
        meme_list = []
        for meme in Memes.select().where(Memes.width == width):
            meme_list.append(model_to_dict(meme))
        if len(meme_list) == 0:
            return jsonify({"Error": "Width not found"})
        else:
            return jsonify(meme_list)


@app.route('/memes/height/<height>', methods=['GET'])
def height(height=None):
    if height:
        meme = Memes.get(Memes.height == height)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/memes/box_count/<box_count>', methods=['GET'])
def box(box_count=None):
    if box_count:
        meme = Memes.get(Memes.box_count == box_count)
        meme = model_to_dict(meme)
        return jsonify(meme)
    else:
        memes = []
        for meme in Memes.select():
            memes.append(model_to_dict(meme))
        return jsonify(memes)


@app.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "Hello GET"})
    else:
        return jsonify({"message": "Hello, world!"})


app.run(port=9000, debug=True)
