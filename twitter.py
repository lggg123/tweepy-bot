import tweepy 
import time 

auth = tweepy.OAuthHandler('##########',
                           '##########')

auth.set_access_token('#####################'),
                      '#####################')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

# to have a lot of pagination of users or followers
# it will gather the list and go through all the users
# we iterate through the followers and then .items gets back 
# all the items 
search = '#comedyclub'
nrTweets = 500

for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
    try:
        print('tweet liked')
        tweet.favorite()
        time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break 
