import tweepy
import credentials as cred
import retweets

consumer_key = cred.consumer_key
consumer_secret = cred.consumer_secret
access_token = cred.access_token
access_token_secret = cred.access_token_secret
client_id = cred.client_id
client_secret = cred.client_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_image(image_path, tweet_text):
    # Generate tweet
    api.update_status(image_path, f"{tweet_text}")
    return print("Done")

def tweet_text(tweet_text):
    # Generate tweet
    api.update_status(f"{tweet_text}")
    return print("Done")

def tweet_url(tweet_text, url):
    # Generate tweet
    api.update_status(f"{tweet_text} {url}")
    return print("Done")

def retweet(ID):
    # retweeting the tweet
    api.retweet(ID)
    return print("Done")

def like(ID):
    # liking the tweet
    api.create_favorite(ID)
    return print("Done")

TWEET_COUNT = 0

def rt(api, id):
    global TWEET_COUNT
    if TWEET_COUNT < retweets.MAX_TWEETS:
        try:
            api.retweet(id)
            print("Retweeting: " + str(id))
            TWEET_COUNT = TWEET_COUNT + 1
        except:
            print("Already Retweeted: "+ str(id))
    else:
        print("Exiting Program Max Reached")
        exit()

def retweet_bunch(api, count):
    for handle in retweets.RT_HANDLES:
        tweets = api.user_timeline(screen_name=handle, count = count)
        for tweet in tweets:
            if TWEET_COUNT < retweets.MAX_TWEETS:
                rt(api, tweet.id)
            else:
                print("ERROR")
    return print("Done")