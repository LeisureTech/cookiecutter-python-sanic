from sanic import Sanic
from sanic.response import text
import multiprocessing

from auth.auth import protected
from auth.login import login

app = Sanic("My Hello, world app")
app.config.SECRET = "KEEP_IT_SECRET_KEEP_IT_SAFE"
app.blueprint(login)


@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


@app.get("/secret")
@protected
async def secret(request):
    return text("To go fast, you must be fast.")

if __name__ == "__main__":
    workers = multiprocessing.cpu_count()
    app.run(host="0.0.0.0", port=8000, workers=workers)
