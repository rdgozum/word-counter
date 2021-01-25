# Word Counter
An API which counts how many times a word exists in the webpage source. Link to the [docs](https://github.com/rdgozum/word-counter/tree/main/docs/api.md).

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
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
```
- Run this command in your terminal to serve the Flask app:
```bash
$ flask run
```
- In a separate tab, run this command to send a POST request to the server. You can also use other API testing tools such as Postman:
```
$ curl -X POST \
    -H "Content-type: application/json" \
    -d '{"word": "fit","url": "https://virtusize.jp"}' \
    "localhost:5000/wordcount"
```

## Unit Test
- Perform unit testing on the Flask app:
```
$ python -m pytest
```
