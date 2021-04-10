from quart import Quart

app = Quart(__name__)


@app.route('/')
async def helloWorld():
    return 'hello World!'


app.run()