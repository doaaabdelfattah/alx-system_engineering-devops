#!/usr/bin/python3
'''
returns the number of subscribers
'''
import requests


def number_of_subscribers(subreddit):
    ''' returns the number of subscribers
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Make a GET request to fetch user information
    response_user = requests.get(f'{url}',
                                 headers=headers,
                                 allow_redirects=False)
    # Extracts the JSON content from the HTTP response
    # It return a Python dict that can be accessed
    data = response_user.json()
    return data['data']['subscribers']
