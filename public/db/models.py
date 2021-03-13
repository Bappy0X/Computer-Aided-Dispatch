from flask import Flask

#Our MongoEngine libraries
from flask_mongoengine import MongoEngine
import mongoengine_goodjson as gj
from mongoengine.fields import ObjectIdField, ObjectId
from mongoengine.errors import ValidationError

db = MongoEngine()

class User(gj.Document):
    meta = {
        "collection": "Users"
    }
    ...

class Update(gj.Document):
    meta = {
        "collection": "Updates"
    }
    ...

class Call(gj.Document):
    meta = {
        "collection": "Calls"
    }

    name = db.StringField()
    description = db.StringField()
    manager = db.ReferenceField(User)
    assigned = db.ListField(db.ReferenceField(User))
    status = db.StringField()
    updates = db.ListField(db.ReferenceField(Update))
