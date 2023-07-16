#!/usr/bin/python3
""" 3-count.py """
import json
import requests


def count_words(subreddit, word_list, after="", count=None):
    """ prints a sorted count of given keywords """

    if count is None:
        count = [0] * len(word_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'User-Agent': 'Mozilla/5.0'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(word_list)):
                    if word_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(word_list)):
                for j in range(i + 1, len(word_list)):
                    if word_list[i].lower() == word_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            sorted_counts = sorted(zip(word_list, count), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0 and word_list.index(word) not in save:
                    print("{}: {}".format(word.lower(), count))
        else:
            count_words(subreddit, word_list, after, count)
