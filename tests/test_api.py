import json

from word_counter.models import CountModel


def test_word_count_success(test_app):
    test_client, _ = test_app

    # DB state before the API call
    db_content = CountModel.query.first()
    assert db_content is None

    # API Call
    payload = {"word": "fit", "url": "https://virtusize.jp"}
    response = test_client.post(
        "/wordcount", data=json.dumps(payload), content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data["count"] == 12
    assert data["status"] == "ok"

    # DB state after the API call
    db_content = CountModel.query.first()
    assert db_content.word == "fit"
    assert db_content.url == "https://virtusize.jp"
    assert db_content.count == 12


def test_word_count_400(test_app):
    test_client, _ = test_app

    # API Call
    payload = {"url": "https://virtusize.jp"}
    response = test_client.post(
        "/wordcount", data=json.dumps(payload), content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert data["status"] == 400


def test_word_count_404(test_app):
    test_client, _ = test_app

    # API Call
    payload = {"word": "fit", "url": "https://virtusize.jp"}
    response = test_client.post(
        "/nonexisting/route", data=json.dumps(payload), content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 404
    assert data["status"] == 404


def test_word_count_500(test_app):
    test_client, _ = test_app

    # API Call
    payload = {"word": "fit", "url": "https://whatisthis.com"}
    response = test_client.post(
        "/wordcount", data=json.dumps(payload), content_type="application/json",
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 500
    assert data["status"] == 500
