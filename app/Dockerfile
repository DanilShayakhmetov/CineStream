FROM python:3

COPY . /app

RUN apt-get update; apt-get install -y locales locales-all

RUN pip install -r /app/requirements.txt

ENV LC_ALL ru_RU.UTF-8
ENV LANG ru_RU.UTF-8
ENV LANGUAGE ru_RU.UTF-8

ENV PYTHONPATH .
ENV FLASK_APP runserver.py
ENV FLASK_DEBUG 0

WORKDIR /app

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=80"]