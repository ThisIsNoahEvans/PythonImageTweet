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

auth = tweepy.OAuthHandler("Xh1X0RgIuFmH14zkrCagFBfUH", "jHiX0qvRmVGKILKxBIE91sB3HFR3cMci846fYYBdChUjcp6Tbi")
auth.set_access_token("896644687301414913-BjZiL8OdijzcUouJ29tCUjIO2L1RPOz", "gkhg43hubis8hYSL1FPMd1XS5CfUd99nfoIX2uRoJhylt")
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

