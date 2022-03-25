FROM python:3.9.5-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]