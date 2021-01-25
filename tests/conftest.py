import pytest

from word_counter import create_app, db
from word_counter.config import Config


@pytest.fixture(scope="module")
def app():
    flask_app = create_app(Config)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            db.create_all()
            yield testing_client, db
            db.drop_all()
            db.session.commit()
