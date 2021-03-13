from flask import Blueprint, request, jsonify, abort

from sys import path
path.append("...")

from public.db.models import User

blueprint = Blueprint("objects", __name__)

@blueprint.route("/calls")
def calls():
    """
        <h3>This is a test</h3>
        <p>Test return</p>
    """
    res = User.objects.paginate(page=1, per_page=10)
    print(res)
    print(res.items)
    return jsonify(res.items)