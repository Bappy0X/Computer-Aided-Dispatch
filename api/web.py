"""from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS

from dotenv import load_dotenv
load_dotenv()
from os import getenv, listdir
from importlib import import_module

from public.db.models import db"""

from fastapi import FastAPI

app = FastAPI()
"""CORS(app)

app.config["MONGODB_HOST"] = getenv("MONGODB_HOST")
db.init_app(app)

for i in [i[:-3] for i in listdir("views") if i != "__pycache__"]:
    thisModule = import_module(f"views.{i}")
    app.register_blueprint(thisModule.blueprint)

#Error Handlers
@app.errorhandler(404)
def not_found(description):
    error = 404
    description = str(description)
    return jsonify(**locals()), error"""

from routes import routers
for i in routers:
    app.include_router(i)