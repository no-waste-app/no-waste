FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7

RUN apk --update add bash nano

WORKDIR /app

# copy the dependencies file to the working director                                                                                                                                                                                         COPY ./requirements.txt /app/requirements.txt 

RUN pip install -r  app/requirements.txt

COPY . /app

# start
CMD [ "python", "no_waste.py" ]
