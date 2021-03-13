from flask import Blueprint, request, jsonify, url_for

from sys import path
path.append("...")

from public.db.models import Call, ValidationError

from json import loads

blueprint = Blueprint("objects", __name__)

@blueprint.route("/calls", methods=["GET", "POST"])
def calls():
    """
        ## [GET] List our calls.

            - Query/URL Params:
                - "perpage":
                    - Description: How many records are returned, per page
                    - Default: 1
                    - Datatype: Int
                - "page":
                    - Description: The current page cursor.
                    - Default: 1
                    - Datatype: Int

            - Example:
                - `/calls?page=1&perpage=5`

            - Responses:
                - 404: Invalid page number.

        ## [POST] Create a new call.
            
            - Multipart Form Data:
                - "name": The name for the new call
                - "description": A description for this new call
    """
    if request.method == "GET":
        perPage = request.args.get("perpage", 5, int)
        page    = request.args.get("page",    1, int)

        res = Call.objects().limit(perPage).skip(perPage*(page-1))
        return jsonify(
            success = True,
            data = [loads(i.to_json()) for i in res],#follow_reference=True
            lastPage = url_for("objects.calls", perPage=perPage, page=page-1),
            nextPage = url_for("objects.calls", perPage=perPage, page=page+1)
        )
    elif request.method == "POST":
        obj = Call(name="testtt")
        obj.save()
        return jsonify(success=True, call=obj)

@blueprint.route("/calls/<string:id>")
def getCall(id):
    """
        ## [GET] Fetch the data for a specific call

            - URL Vars:
                - "id": The id for the call to fetch.
    """
    try:
        thisCall = Call.objects.get(id=id)
    except ValidationError:
        return jsonify(success=False, error="Invalid ID!")
    return jsonify(loads(thisCall.to_json()))#follow_reference=True