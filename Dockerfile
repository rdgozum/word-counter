FROM python:3.7.4-slim

ENV PROJECT_DIRECTORY=/home/app
RUN mkdir -p $PROJECT_DIRECTORY
RUN mkdir -p $PROJECT_DIRECTORY/static

WORKDIR $PROJECT_DIRECTORY
COPY requirements.txt $PROJECT_DIRECTORY
RUN pip install -r requirements.txt
COPY . $PROJECT_DIRECTORY

ENTRYPOINT ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:5000", "run:app"]
