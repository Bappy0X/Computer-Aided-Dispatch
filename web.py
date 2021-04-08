from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS

from dotenv import load_dotenv
load_dotenv()
from os import getenv

from public.db.models import db

def createApp():
    app = Flask(__name__)
    CORS(app)

    app.config["MONGODB_HOST"] = getenv("MONGODB_HOST")
    db.init_app(app)

    from views.main import blueprint as mainBlueprint
    app.register_blueprint(mainBlueprint)

    from views.calls import blueprint as callsBlueprint
    app.register_blueprint(callsBlueprint)

    #Error Handlers
    @app.errorhandler(404)
    def not_found(description):
        error = 404
        description = str(description)
        return jsonify(**locals()), error

    return app

if __name__ == "__main__":
    createApp().run(host="0.0.0.0", port=80, debug=True)