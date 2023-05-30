FROM python:3.10-alpine

WORKDIR /usr/src/py_app

COPY . .

ARG MESSAGE
ENV message=${MESSAGE}

RUN pip install -r requirements.txt

CMD [ "hypercorn", "app:asgi_app" ]