from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

class User(db.Document):
    email = db.StringField()
    password = db.StringField()
    fullName = db.StringField()
    userLevel = db.StringField()
    currentPos = db.StringField()
    lastUpdate = db.StringField()