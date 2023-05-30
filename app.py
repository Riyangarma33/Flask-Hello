from asgiref.wsgi import WsgiToAsgi
from flask import Flask
from os import environ

app = Flask(__name__)

@app.route('/')
async def hello() -> str:
    return environ.get('message') if 'message' in environ else 'Hello World!'

asgi_app = WsgiToAsgi(app)

# Use hypercorn to serve
# hypercorn app:asgi_app