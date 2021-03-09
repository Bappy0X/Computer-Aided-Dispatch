from flask import Flask, jsonify, request, render_template_string
from flask_cors import CORS

from os import getenv

def createApp():
    app = Flask(__name__)

    app.jinja_env.globals.update({

    })

    CORS(app)

    from views.main import blueprint as mainBlueprint
    app.register_blueprint(mainBlueprint)

    #Error Handlers
    @app.errorhandler(404)
    def not_found(description):
        error = 404
        description = str(description)
        return jsonify(**locals()), error

    @app.route("/")
    def index():
        return jsonify({"success": True})

    return app

if __name__ == "__main__":
    createApp().run(host="0.0.0.0", port=80, debug=True)