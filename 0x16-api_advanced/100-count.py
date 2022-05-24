#!/usr/bin/python3
"""  function that queries the Reddit API;
and print ten titles """
from operator import itemgetter
import requests


def count_words(subreddit, word_list):
    """ count words """
    try:
        list_T = []
        my_dict = {}
        hot_list = recurse(subreddit, list_T)
        str_word = " ".join(word_list).lower()
        word_list = str_word.split()
        str_list = " ".join(hot_list).lower()
        for word in word_list:
            n = str_list.split().count(word)
            if my_dict.get(word):
                my_dict[word] = my_dict[word] + n
            else:
                my_dict[word] = n
        sort_dict = dict(sorted(my_dict.items(),
                                key=itemgetter(1), reverse=True))
        for k, v in sort_dict.items():
            if v > 0:
                print("{}: {}".format(k, v))
    except Exception:
        pass


def recurse(subreddit, hot_list=[], after=""):
    """ return list of title """
    header = {'User-Agent': 'my_user_agent'}
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit,
                                                                 after)
    try:
        response = requests.get(url, headers=header,
                                allow_redirects=False).json().get("data")
        after = response.get("after", None)
        for children in response.get("children"):
            hot_list.append(children.get("data").get("title"))
        if after is not None:
            recurse(subreddit, hot_list, after)
        return(hot_list)
    except Exception:
        return(None)
