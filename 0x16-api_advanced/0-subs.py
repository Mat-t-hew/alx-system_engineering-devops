#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Python/1.0(Alx Project)"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return "OK"
    elif response.status_code == 404:
        return 0
    else:
        return "Failed"

# Example usage:
subreddit = "learnpython"
result = number_of_subscribers(subreddit)
print(result)
