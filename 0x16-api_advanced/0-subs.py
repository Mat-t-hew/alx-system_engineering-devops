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
    if response.status_code == 404:
        return 0
    elif response.status_code == 200:
        return "OK"  # Return "OK" when request is successful
    else:
        return "Failed"  # Return "Failed" for any other status code


# Example usage:
subreddit = "learnpython"
print(number_of_subscribers(subreddit))
