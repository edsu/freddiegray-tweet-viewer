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
parser.add_argument('--include_retweets', action="store_true", help='include retweets') 
parser.add_argument('--min_retweet', type=int, default=0, help='only include tweets that have at least been tweeted n times')
parser.add_argument('--include_dupes', action="store_true", help='remove duplicate images')
parser.add_argument('--text', action="store_true", help='only output ids')
args = parser.parse_args()

if not args.text:
    print 'var ids = ['

media_seen = set()
for line in open(args.filename):
    try:
        tweet = json.loads(line)
    except:
        continue
    if 'retweeted_status' in tweet and not args.include_retweets:
        continue
    if tweet['retweet_count'] < args.min_retweet:
        continue
    if 'media' not in tweet['entities']:
        continue

    if not args.include_dupes:
        media_url = tweet['entities']['media'][0]['media_url_https']
        if media_url in media_seen:
            continue
        media_seen.add(media_url)

    if args.text:
        print tweet['id_str']
    else:
        print '  "%s",' % tweet['id_str']

if not args.text:
    print '];'
