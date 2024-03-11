#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers.
"""
import requests

def number_of_subscribers(subreddit):
    """Initialize"""
    if not isinstance(subreddit, str):
        print("Invalid subreddit:", subreddit)
        return 0

    url_api = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'safari:holberton/0.1.0'}
    
    print("Request URL:", url_api)
    response = requests.get(url_api, headers=headers)
    print("Response status code:", response.status_code)

    if response.status_code != 200:
        print("Failed to get data from API")
        return 0
    
    data = response.json().get("data")
    if data is None:
        print("No data received from API")
        return 0

    subscribers = data.get("subscribers")
    print("Number of subscribers:", subscribers)
    return subscribers

# Test the function
subreddit = "learnpython"
print("The number of subscribers in r/{} is: {}".format(subreddit, number_of_subscribers(subreddit)))
