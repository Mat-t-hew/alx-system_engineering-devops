#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Initialize and query the Reddit API to get the number of subscribers
    for the given subreddit.

    Args:
        subreddit: A string representing the subreddit name.

    Returns:
        The number of subscribers if successful, otherwise 0.
    """
    if not isinstance(subreddit, str):
        return 0

    url_api = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Python/1.0(Alx Project)'}
    response = requests.get(url_api, headers=headers)

    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    subscribers = data.get("subscribers", 0)
    return subscribers

# Example usage:
subreddit = "learnpython"
subscribers = number_of_subscribers(subreddit)
