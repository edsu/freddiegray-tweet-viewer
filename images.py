#!/usr/bin/env python

"""
images.py will read a file of tweets and write out a javascript array containing
tweet ids for original tweets that contain images that have been retweeted at 
leaset once. You can control the knobs with command line options.
"""

import json
import argparse

parser = argparse.ArgumentParser(description="filter image tweets")
parser.add_argument('filename', type=str, help='json file for tweets')
parser.add_argument('--retweets', type=bool, default=False, help='include retweets') 
parser.add_argument('--min_retweet', type=int, default=1, help='only include tweets that have at least been tweeted n times')
parser.add_argument('--remove_dupes', type=bool, default=True, help='remove duplicate images')
args = parser.parse_args()

print 'var ids = ['

media_seen = set()
for line in open(args.filename):
    try:
        tweet = json.loads(line)
    except:
        continue
    if 'retweet_status' in tweet:
        continue
    if tweet['retweet_count'] < args.min_retweet:
        continue
    if 'media' not in tweet['entities']:
        continue

    if args.remove_dupes:
        media_url = tweet['entities']['media'][0]['media_url_https']
        if media_url in media_seen:
            continue
        media_seen.add(media_url)

    print '  "%s",' % tweet['id_str']

print '];'
