#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """returns total subscribers"""
    rq = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        header={"User-Agent": "Mozilla"},
    )

    if rq.status_code == 200:
        return rq.json().get("data").get("subscribers")
    else:
        return 0
