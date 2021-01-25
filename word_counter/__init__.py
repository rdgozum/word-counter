from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    with app.app_context():
        from word_counter.main.routes import main
        from word_counter.errors.handlers import errors

        app.register_blueprint(main)
        app.register_blueprint(errors)
        db.create_all()

        return app
