import urllib.request
import re

from flask import abort


def counter_method(word, url):
    """
    This function calculates word frequency from a page source accepting two parameters word and url.

    Parameters
    ----------
    word : str
        The word we want to count from the page source.
    url : str
        The website we want to extract the source text from.

    Returns
    -------
    count : int
        The frequency of word from the page source.
    """

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
