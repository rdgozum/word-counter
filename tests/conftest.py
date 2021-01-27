import pytest

from word_counter import create_app, db as test_db
from word_counter.config import TestingConfig


@pytest.fixture(scope="module")
def test_app():
    app = create_app(TestingConfig)

    # Create a test client using the Flask application configured for testing
    with app.test_client() as test_client:
        # Establish an application context
        with app.app_context():
            test_db.create_all()
            yield test_client, test_db
            test_db.drop_all()
            test_db.session.commit()
