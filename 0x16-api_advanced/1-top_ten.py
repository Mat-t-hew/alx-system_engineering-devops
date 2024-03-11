#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first ten hot posts
for a given subreddit
"""
import requests


def top_ten(subreddit):
    if not isinstance(subreddit, str):
        print("None")
        return
    
    url_api = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'safari:schoolalx/0.7.4'}
    response = requests.get(url_api, headers=headers)
    
    if response.status_code != 200:
        print("None")
        return
    
    posts_json = response.json().get("data", {}).get("children", [])
    
    for i in range(min(10, len(posts_json))):
        post_title = posts_json[i].get("data", {}).get("title", "")
        print(post_title)
