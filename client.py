import tweepy
import os

#Sets Font For Print
class colour:
    purple = '\033[95m'
    green = '\033[92m'
    red = '\033[91m'
    blue = '\033[94m'
    bold = '\033[1m'
    end = '\033[0m'

auth = tweepy.OAuthHandler("api", "api")
auth.set_access_token("api", "api")
api = tweepy.API(auth)
print(colour.purple, 'Connected to APIs', colour.end)

# Upload image
print(colour.bold, colour.blue)
image = input('Drag in image path, or press enter to Tweet without an image: ')
print(colour.end)
if image == '':
    print(colour.bold, colour.blue)
    tweet = input('Enter Tweet: ')
    print(colour.end)
    try:
        post_result = api.update_status(tweet)
        print(colour.bold, colour.green, 'TWEETED:', colour.end, colour.green, tweet, colour.end)
    except:
        print(colour.bold, colour.red, 'There was an error sending the Tweet', colour.end)
else:
    print(colour.bold, colour.green, 'Uploading image...', colour.end)
    media = api.media_upload(image)
    print(colour.bold, colour.blue)
    tweet = input('Enter Tweet: ')
    print(colour.end)
    post_result = api.update_status(status=tweet, media_ids=[media.media_id])   
    print(colour.bold, colour.green, 'TWEETED:', colour.end, colour.green, tweet, colour.end)

