# syntax=docker/dockerfile:1

FROM dvcorg/cml-py3 as base
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY . ./app

FROM python:3.8-slim-buster
COPY --from=base /app /app
WORKDIR /app
RUN pip3 install -r requirements.txt 

EXPOSE 8080

CMD [ "python3", "./app/app.py"]
