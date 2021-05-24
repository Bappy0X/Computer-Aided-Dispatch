from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def index():
    """
        ## Get basic hello world message
    """
    return {"success": True, "value": "Hello World!"}