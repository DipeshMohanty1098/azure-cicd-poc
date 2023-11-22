FROM python:3.8-slim-buster

WORKDIR /python-docker-azure-poc

COPY requirements.txt requirements.txt
RUN /bin/bash -c "source test/Scripts/activate; pip install -r requirements.txt"

COPY . .

ENTRYPOINT /bin/bash -c "test/Scripts/activate; python app.py"