# Word Counter
An API which counts how many times a word exists in the webpage source. Link to the documentation [here](https://github.com/rdgozum/word-counter/tree/main/docs/api.md).

## Setup
Run the commands below to setup your local environment.

## Prerequisites
```bash
$ git clone git@github.com:rdgozum/word-counter.git
$ cd word-counter
$ pip install -r requirements.txt
```

## Project Usage
- Add a **.env** file inside your project root.
```
FLASK_APP=run.py
FLASK_DEBUG=1
SECRET_KEY=<alphanumeric string>
SQLALCHEMY_DATABASE_DEV_URI=sqlite:///site-dev.db
SQLALCHEMY_DATABASE_TEST_URI=sqlite:///site-test.db
```
- Run this command in your terminal to serve the Flask app:
```bash
$ flask run
```
- In a separate tab, run this command to send a POST request to the server. You can also use other API testing tools such as Postman:
```
$ curl -X POST \
    -H "Content-type: application/json" \
    -d '{"word": "fit", "url": "https://virtusize.jp"}' \
    "localhost:8080/wordcount"
```

## Unit Test
- Perform unit testing on the Flask app:
```
$ python -m pytest
```

## Deploy App
Run nginx and flask_app containers using docker-compose command. Once running, the API can be accessed via curl command or browser from any device within the local network.
- *Build/Run:* `docker-compose up --build`
- *Check containers status:* `docker-compose ps`
- *Stop running containers:* `docker-compose kill`
- *Remove stopped containers:* `docker-compose rm -f`
