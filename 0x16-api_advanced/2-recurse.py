#!/usr/bin/python3
'''
returns the number of subscribers
'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    ''' returns the number of subscribers
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # Make a GET request to fetch subreddit information
    response = requests.get(url, params={"after": after},
                            allow_redirects=False)
    if response.status_code == 404:
        # If subreddit not found, return 0 subscribers
        return None

    # Extract JSON content from the response
    data = response.json()
    #  extracts the value of the "after" key from JSON
    after = data.get('after')
    # Extract the list of posts from the JSON data
    list_data = data['data']
    # Print titles of the top ten posts
    for post in list_data['children']:
        hot_list.append(post.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
