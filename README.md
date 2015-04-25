Displays random tweets from a set of tweet ids stored in `js/ids.js`. If you've
got a file of tweets (line oriented json) that you've collected with something
like [twarc] then you can use the `images.py` program to generate a new 
`js/ids.js` file.

    images.py tweets.json > js/ids.js

`images.py` will filter out only original tweets that have embedded media.
By default it will also remove duplicates of the same media file. So two 
tweets that reference the same media file will only be included once. You 
can control this behavior with command line arguments.

One way of limiting tweets that are displayed can be to limit to only tweets 
that have been retweeted more than say 5 times:

    images.py --min_retweet 5

This can help in situations where people are spamming a hashtag with 
advertising, etc. If you collected your data from the live stream you won't
have the retweet count; but here's a trick for getting the latest
retweet counts for your data.

    # get the ids as a text file
    images.py --text tweets.json > ids.txt

    # hydrate the ids (which gets the latest retweet counts)
    twarc.py --hydrate ids.txt > hydrated.json

    # generate the tweet ids with a minimum of 5 retweets
    images.py --min_retweet 5 hydrated.json > ids.js

Any tweets that have been deleted won't appear in newer_tweets.json. But
you won't be able to display these anyway, so maybe that's a good thing.

[twarc]: http://github.com/edsu/twarc
