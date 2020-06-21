import tweepy 
import time 

auth = tweepy.OAuthHandler('6G36Uzr38DxkPAHlarzZsD6gl',
                           'tkxcbKIJ1sF9vPZIpMUWEONWy8X6VI4BvaYMmif4BOI12orhxo')

auth.set_access_token('481841999-tQFKpVXLwacvJbRQdrLNRmx5Uqcresh6Ggt3k12h',
                      'z4CDVt7y2svEmSSFLXjcRTfwlnog0Jl64oj13EodLsWAo')

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
