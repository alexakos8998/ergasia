import sys
import twitter

CONSUMER_KEY = 'XXXXXXXX'
CONSUMER_SECRET = 'XXXXXXXX'
OAUTH_TOKEN = 'XXXXXXXX'
OAUTH_TOKEN_SECRET = 'XXXXXXXX'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

name1 = sys.argv[1]
name2 = sys.argv[2]
status1 = twitter_api.statuses.user_timeline(count=2, screen_name=name1)
tweets1 = []
for tweet in tweets1:
    tweets1.append(tweet['text'])
status2 = twitter_api.statuses.user_timeline(count=2, screen_name=name2)
tweets2 = []
for tweet in tweets:
    tweets2.append(tweet['text'])
count1 = 0
count2 = 0
for tweet in tweets1:
    count1 += len(tweet)
for tweet in tweets2:
    count2 += len(tweet)
if count1 > count2:
    print(name1, "used more characters")
elif count1 < count2:
    print(name2, "used more characters")
else:
    print("Both used the same amound of characters")