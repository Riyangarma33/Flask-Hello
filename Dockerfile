FROM python:3.10-alpine

WORKDIR /usr/src/py_app

COPY . .

ARG MESSAGE
ENV message=${MESSAGE}

RUN pip install -r requirements.txt

CMD [ "python", "-m", "hypercorn", "app:asgi_app", "--bind", "0.0.0.0:8005" ]