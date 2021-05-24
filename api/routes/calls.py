"""from flask import Blueprint, request, jsonify, url_for

from sys import path
path.append("...")

from public.db.models import Call, Update, ValidationError

from json import loads
from datetime import datetime as dt

blueprint = Blueprint("calls", __name__)"""

from fastapi import APIRouter

from typing import Optional
from pydantic import BaseModel

router = APIRouter()

@router.get("/calls")
def many(perpage: int=1, page: int=1):
    """
        ## List our calls.

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
    """
    return {"success": False}
    """args = request.args
    perPage = args.get("perpage", 5, int)
    page    = args.get("page",    1, int)
    if perPage > 10 or perPage < 0: perPage = 10

    pagination = Call.objects.paginate(page=page, per_page=perPage)
    return jsonify(
        success = True,
        data = [dict(i) for i in pagination.items],
        lastPage = url_for("calls.many", perPage=perPage, page=pagination.page-1) if pagination.page-1 > 0 else None,
        nextPage = url_for("calls.many", perPage=perPage, page=pagination.page+1) if pagination.page+1 <= pagination.pages else None
    )"""

class Call(BaseModel):
    name: str
    description: Optional[str]=None

@router.post("/calls")
def create(call: Call):
    """
        ## Create a new call.
            
        - Multipart Form Data:
            - "name": The name for the new call
            - "description": A description for this new call
    """
    return {"success": False}
    """form = request.form
    for i in ["name", "description"]:
        if not form.get(i):
            return jsonify(success=False, error=f"Missing form field `{i}`.")

    thisCall = Call(
        name=form["name"],
        description=form["description"]
    )

    thisUpdate = Update(
        title="Call Created",
        description="This call was created.",
        timestamp=dt.now()
    )
    thisUpdate.save()

    thisCall.updates.append(thisUpdate)
    thisCall.save()

    return jsonify(success=True, call=dict(thisCall))"""
    
@router.get("/calls/<string:_id>")
def one(callId: int):
    """
        ## Fetch the data for a single call

        - URL Vars:
            - "_id": The id for the call to fetch.
        - Example:
            - `/calls/1234567890`
    """
    return {"success": False}
    """try:
        thisCall = Call.objects.get(id=_id)
    except ValidationError:
        return jsonify(success=False, error="Invalid ID!")
    return jsonify(dict(thisCall))"""