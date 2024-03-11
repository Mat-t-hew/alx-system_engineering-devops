#!/usr/bin/python3
"""
function that queries the Reddit API
and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """initializate"""
    if not isinstance(subreddit, str):
        return 0
    url_api = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'python3:holberton'}
    response = requests.get(url_api, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    try:
        data = response.json().get("data", {}).get("subscribers", 0)
        return data
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return 0


def validate_output(subreddit, expected_output):
    """Validate the output"""
    result = number_of_subscribers(subreddit)
    if result == expected_output:
        return "OK"
    else:
        return "Failed"


if __name__ == "__main__":
    # Test cases
    output1 = validate_output("existingsubreddit", 0)  # Existing subreddit
    output2 = validate_output("nonexistingsubreddit", 0)  # Non-existing subreddit
    print("Output: existing Subreddit\nScore:", 2 if output1 == "OK" else 0, "out of 2 points")
    print("Output: nonexisting subreddit\nScore:", 2 if output2 == "OK" else 0, "out of 2 points")
    validate_output("nonexistingsubreddit", 0)  # Non-existing subreddit
