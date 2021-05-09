from flask import Flask, url_for

#Our MongoEngine libraries
from flask_mongoengine import MongoEngine
from mongoengine.fields import ObjectIdField, ObjectId
from mongoengine.errors import ValidationError

db = MongoEngine()

class User(db.Document):
    meta = {
        "collection": "Users"
    }
    email = db.EmailField()
    password = db.StringField()
    fullName = db.StringField()
    userLevel = db.IntField()
    currentPos = db.GeoPointField()
    lastUpdate = db.DateTimeField()

    def __iter__(self):
        yield "id", str(self.id)
        yield "email", self.email
        yield "fullName", self.fullName
        yield "userLevel", self.userLevel

class Update(db.Document):
    meta = {
        "collection": "Updates"
    }
    title = db.StringField()
    description = db.StringField()
    user = db.ReferenceField(User)
    timestamp = db.DateTimeField()

    def __iter__(self):
        yield "id", str(self.id)
        yield "title", self.title
        yield "description", self.description
        yield "user", self.user
        yield "timestamp", self.timestamp

class Call(db.Document):
    meta = {
        "collection": "Calls"
    }

    name = db.StringField()
    description = db.StringField()
    manager = db.ReferenceField(User)
    assigned = db.ListField(db.ReferenceField(User))
    status = db.StringField()
    updates = db.ListField(db.ReferenceField(Update))

    def __iter__(self):
        yield "id", str(self.id)
        yield "name", self.name
        yield "description", self.description
        yield "manager", self.manager
        yield "assigned", [dict(i) for i in self.assigned]
        yield "status", self.status
        yield "updates", [dict(i) for i in self.updates]
        yield "url", url_for("calls.one", _id=self.id)