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
        name_list = []
        for meme in Memes.select().where(Memes.name == name):
            name_list.append(model_to_dict(meme))
            return jsonify(meme)
        if len(name_list) == 0:
            return jsonify({"Error": "Name not found"})
        else:
            return jsonify(name_list)


@app.route('/memes/width/<width>', methods=['GET'])
def width(width=None):
    if width:
        width_list = []
        for meme in Memes.select().where(Memes.width == width):
            width_list.append(model_to_dict(meme))
        if len(width_list) == 0:
            return jsonify({"Error": "Width not found"})
        else:
            return jsonify(width_list)


@app.route('/memes/height/<height>', methods=['GET'])
def height(height=None):
    if height:
        height_list = []
        for meme in Memes.select().where(Memes.height == height):
            height_list.append(model_to_dict(meme))
        if len(height_list) == 0:
            return jsonify({"Error": "Height not found"})
        else:
            return jsonify(height_list)


@app.route('/memes/box_count/<box_count>', methods=['GET'])
def box(box_count=None):
    if box_count:
        box_count_list = []
        for meme in Memes.select().where(Memes.box_count == box_count):
            box_count_list.append(model_to_dict(meme))
        if len(box_count_list) == 0:
            return jsonify({"Error": "Box count not found"})
        else:
            return jsonify(box_count_list)


@app.route('/', methods=['GET', 'PUT', 'POST', 'DELETE'])
def index():
    if request.method == 'GET':
        return jsonify({"message": "Hello GET"})
    else:
        return jsonify({"message": "Hello, world!"})


app.run(port=9000, debug=True)
