import jwt
from sanic import Blueprint, text

login = Blueprint("login", url_prefix="/login")


@login.post("/")
async def do_login(request):
    token = jwt.encode({}, request.app.config.SECRET)
    return text(token)
