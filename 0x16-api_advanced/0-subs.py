#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}  # Set a custom User-Agent
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0

# Example usage:
subreddit = "learnpython"
print(f"The number of subscribers in r/{subreddit} is: {number_of_subscribers(subreddit)}")
