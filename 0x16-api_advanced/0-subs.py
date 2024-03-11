#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """initializate"""
    if (type(subreddit) is not str):
        return(0)
    url_api = ("https://www.reddit.com/r/{}/about.json".format(subreddit))
    headers = {'User-Agent': 'python3:holberton'}
    response = requests.get(url_api, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return(0)
    data = response.json().get("data", {}).get("subscribers", 0)
    return data


def validate_output(subreddit, expected_output):
    """Validate the output"""
    result = number_of_subscribers(subreddit)
    if result == expected_output:
        print("OK")
    else:
        print("Failed")


if __name__ == "__main__":
    # Test cases
    validate_output("existingsubreddit", 0)  # Existing subreddit
    validate_output("nonexistingsubreddit", 0)  # Non-existing subreddit
