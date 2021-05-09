from flask import Blueprint, request, jsonify, abort

from sys import path
path.append("...")

blueprint = Blueprint("main", __name__)

@blueprint.route("/")
def home():
    """
        <h3>This is a test</h3>
        <p>Test return</p>
    """
    return jsonify({"success": True, "value": "Hello World!"})