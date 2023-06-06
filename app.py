from asgiref.wsgi import WsgiToAsgi
from flask import Flask
from ast import literal_eval
from os import environ

app = Flask(__name__)

@app.route('/')
async def hello() -> str:
    ret_msg : str
    if 'message' in environ:
        ret_msg = environ.get('message')
        try: 
            eval_msg = literal_eval(ret_msg)
            ret_msg += f'\n{eval_msg}'
        except ValueError as err:
            ret_msg += f'\n{err}'
    else:
        ret_msg = 'Hello World!'
    return ret_msg

asgi_app = WsgiToAsgi(app)

# Use hypercorn to serve
# hypercorn app:asgi_app