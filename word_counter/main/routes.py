from flask import request, jsonify, abort
from flask import Blueprint

from word_counter import db
from word_counter.models import CountModel
from word_counter.main.utils import counter_method

main = Blueprint("main", __name__)


@main.route("/wordcount", methods=["GET", "POST"])
def word_count():
    """
    This function calculates word frequency from a page source accepting payload in JSON format.

    Example
    -------
    curl -X POST \
      -H "Content-type: application/json" \
      -d '{"word": "fit","url": "https://virtusize.jp"}' \
      "localhost:5000/wordcount"

    Expected Success Response
    -------------------------
    HTTP Status Code: 200

    {
      "count": 12,
      "status": "ok"
    }
    """

    word = request.json.get("word")
    url = request.json.get("url")

    # Check if request parameters are nonempty
    if not word or not url:
        abort(400)

    # Check if there is db entry
    cached = CountModel.query.filter_by(word=word, url=url).first()
    if cached:
        return jsonify(count=cached.count, status="ok")

    # Call the counter method
    count = counter_method(word, url)

    # Save to db if found
    entry = CountModel(word=word, url=url, count=count)
    db.session.add(entry)
    db.session.commit()

    return jsonify(count=count, status="ok")
