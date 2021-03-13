from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS

from os import getenv
from public.db.models import db

def createApp():
    app = Flask(__name__)

    app.config["MONGODB_SETTINGS"] = {
        "db": "joshuavaughan_computer-aided-dispatch",
        "host": "localhost",
        "port": 27017
    }
    db.init_app(app)

    app.jinja_env.globals.update({

    })

    CORS(app)

    from views.main import blueprint as mainBlueprint
    app.register_blueprint(mainBlueprint)

    from views.objects import blueprint as objectsBlueprint
    app.register_blueprint(objectsBlueprint)

    #Error Handlers
    @app.errorhandler(404)
    def not_found(description):
        error = 404
        description = str(description)
        return jsonify(**locals()), error

    return app

if __name__ == "__main__":
    createApp().run(host="0.0.0.0", port=80, debug=True)