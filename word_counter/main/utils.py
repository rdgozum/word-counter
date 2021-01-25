import urllib.request
import re

from flask import abort


def counter_method(word, url):
    try:
        # Extract HTML text
        web_url = urllib.request.urlopen(url)
        html_text = web_url.read().decode("utf-8")

        # Count word matches against HTML text
        pattern = re.compile(r"\b{}\b".format(word))
        matches = list(pattern.finditer(html_text))

        count = len(matches)

        return count
    except:
        abort(500)
