FROM python:3.6-alpine
RUN apk add --update bash
ADD . /code
WORKDIR /code
RUN apk add --update py3-pip
RUN apk --no-cache --update-cache add python-dev py-numpy gcc gfortran postgresql-dev musl-dev freetype-dev
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["sender/wait-for-it.sh", "rabbit:5672", "--", "python3", "sender/app.py"]
