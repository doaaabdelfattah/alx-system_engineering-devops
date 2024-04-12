#!/usr/bin/python3
'''
returns the number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    ''' returns the number of subscribers
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Make a GET request to fetch subreddit information
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        # Extract JSON content from the response
        data = response.json()
        # Extract the number of subscribers from the JSON data
        subscribers = data['data']['subscribers']
        return subscribers
    elif response.status_code == 404:
        # If subreddit not found, return 0 subscribers
        return 0
