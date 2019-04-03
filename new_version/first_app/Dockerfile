FROM python:3.6-alpine
RUN apk add --update bash
ADD . /code
COPY . /code
WORKDIR /code
RUN apk add --update py3-pip
RUN apk --no-cache --update-cache add python-dev py-numpy gcc gfortran postgresql-dev musl-dev freetype-dev
RUN pip install -r requirements.txt

ENV FLASK_APP /code/app.py

CMD ["/code/wait-for-it.sh", "rabbit:5672", "--", "flask", "run"]
