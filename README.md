Displays random tweets from a set of tweet ids stored in `js/ids.js`. If you've
got a file of tweets (line oriented json) that you've collected with something
like [twarc] then you can use the `images.py` program to generate a new 
`js/ids.js` file.

    images.py tweets.json > js/ids.js

`images.py` will filter out only original tweets that have embedded media, and
which have been retweeted at least once. By default it will also remove
duplicates of the same media file. So two tweets that reference the same
media file will only be included once. You can control this behavior with
command line arguments.

[twarc]: http://github.com/edsu/twarc
