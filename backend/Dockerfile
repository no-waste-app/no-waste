FROM python:3.9-alpine

WORKDIR /app

ADD . /app/backend
RUN pip install -r backend/requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "backend.no_waste:app"]