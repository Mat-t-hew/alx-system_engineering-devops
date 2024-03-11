#!/usr/bin/env python3
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
    headers = {'User-Agent': 'python:reddit_subscribers:v1.0.0 (by /u/bdov_)'}
    response = requests.get(url_api, headers=headers)

    if response.status_code != 200:
        print("Request URL:", url_api)
        print("Response status code:", response.status_code)
        print("Failed to get data from API")
        return 0

    data = response.json().get("data", {})
    subscribers = data.get("subscribers", 0)
    print("Request URL:", url_api)
    print("Response status code:", response.status_code)
    print("Number of subscribers:", subscribers)
    return subscribers

# Example usage:
subreddit = "learnpython"
print("Subscribers: {}".format(subreddit, number_of_subscribers(subreddit)))
