#!/usr/bin/python3
'''
returns the number of subscribers
'''
import requests


def top_ten(subreddit):
    ''' returns the number of subscribers
    '''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    # Make a GET request to fetch subreddit information
    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        # Extract JSON content from the response
        data = response.json()
        # Extract the list of posts from the JSON data
        list_data = data['data']['children']
        # Print titles of the top ten posts
        for post in list_data[:10]:
            title = post['data']['title']
            print(title)
        return

    elif response.status_code == 404:
        # If subreddit not found, return 0 subscribers
        print('None')
