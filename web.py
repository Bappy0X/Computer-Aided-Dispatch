from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS

from dotenv import load_dotenv
load_dotenv()
from os import getenv, listdir
from importlib import import_module

from public.db.models import db

def createApp():
    app = Flask(__name__)
    CORS(app)

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
        return jsonify(**locals()), error

    return app

if __name__ == "__main__":
    createApp().run(host="0.0.0.0", port=80, debug=True)