#from hn import HN

#hn = HN()

# get top 20 users of HN
#hn.get_leaders(limit=20)
#print(leader.rank, leader.id)

# print the first 2 pages of newest stories
#for story in hn.get_stories(story_type='newest', limit=10):
#    print(story.rank, story.title)

import time
import urllib.request
import json

author = 'pg'
num_posts =  0
base_url = 'https://hacker-news.firebaseio.com/v0/item/'

for itemid in range(1, 10):
    # Get item
    item_response = urllib.request.urlopen(base_url + str(itemid) + '.json')
    response_string = item_response.readall().decode('utf-8')
    item = json.loads(response_string)
    
    # Increment number of posts by author if they wrote this post
    if item['by'] == author:
        num_posts += 1
        
    # No one likes to be rate limited
    time.sleep(1)

print('Posts by {:s}: {:d}'.format(author, num_posts))