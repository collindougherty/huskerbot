import tweepy
import credentials as cred

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
