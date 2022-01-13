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
    width = IntegerField()
    height = IntegerField()
    box_count = IntegerField()


db.connect()
db.drop_tables([Meme])
db.create_tables([Meme])

meme1 = Meme(name='Drake Hotline Bling', url='https://i.imgflip.com/30b1gx.jpg',
             width=1200, height=1200, box_count=2)
meme2 = Meme(name='Two Buttons', url='https://i.imgflip.com/1g8my4.jpg',
             width=600, height=908, box_count=3)
meme3 = Meme(name='Distracted Boyfriend', url='https://i.imgflip.com/1ur9b0.jpg',
             width=1200, height=800, box_count=3)
meme4 = Meme(name='Running Away Balloon', url='https://i.imgflip.com/261o3j.jpg',
             width=761, height=1024, box_count=2)
meme5 = Meme(name='UNO Draw 25 Cards', url='https://i.imgflip.com/3lmzyx.jpg',
             width=500, height=494, box_count=2)
meme6 = Meme(name='Left Exit 12 Off Ramp', url='https://i.imgflip.com/22bdq6.jpg',
             width=804, height=767, box_count=3)
meme7 = Meme(name='Change My Mind', url='https://i.imgflip.com/24y43o.jpg',
             width=482, height=361, box_count=2)
meme8 = Meme(name='Batman Slapping Robin', url='https://i.imgflip.com/9ehk.jpg',
             width=400, height=387, box_count=2)
meme9 = Meme(name='Woman Yelling At Cat', url='https://i.imgflip.com/345v97.jpg',
             width=680, height=438, box_count=2)
meme10 = Meme(name='Waiting Skeleton', url='https://i.imgflip.com/2fm6x.jpg',
              width=298, height=403, box_count=2)
meme1.save()
meme2.save()
meme3.save()
meme4.save()
meme5.save()
meme6.save()
meme7.save()
meme8.save()
meme9.save()
meme10.save()

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
def width(width=None):
    if width:
        meme = Meme.get(Meme.width == width)
        meme = model_to_dict(meme)
        return jsonify(meme)
    memes = []
    for meme in Meme.select():
        memes.append(model_to_dict(meme))
    return jsonify(memes)


@app.route('/height/<height>', methods=['GET'])
def height(height=None):
    if height:
        meme = Meme.get(Meme.height == height)
        meme = model_to_dict(meme)
        return jsonify(meme)
    memes = []
    for meme in Meme.select():
        memes.append(model_to_dict(meme))
    return jsonify(memes)


@app.route('/box_count/<box_count>', methods=['GET'])
def box(box_count=None):
    if box_count:
        meme = Meme.get(Meme.box_count == box_count)
        meme = model_to_dict(meme)
        return jsonify(meme)
    memes = []
    for meme in Meme.select():
        memes.append(model_to_dict(meme))
    return jsonify(memes)


app.run(port=9000, debug=True)
