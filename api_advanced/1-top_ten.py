#!/usr/bin/python3
"""
Function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """returns first 10 posts"""
    header = {"User-Agent": "Mozilla"}
    url = "https://www.reddit.com/rq/" + subreddit + "/hot.json?limit=10"
    rq = requests.get(url, headers=header, allow_redirects=False)
    if rq.status_code == 200:
        for i in rq.json().get("data", None).get("children", None):
            print(i.get("data", None).get("title", None))
    else:
        print(None)

if __name__ == "__main__":
    pass
