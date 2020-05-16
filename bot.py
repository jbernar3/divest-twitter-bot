import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("XPA1oAPJlwclR2vGEXLsE8z0N",
    "SxDSDLjAmn9ZvBH9PBeHJkTPLhQIRlVP5m522JTZ6AriOenApw")
auth.set_access_token("1261713765063700481-bCrAttUicfuNpOtqrCRz14byxdz3HE",
    "hldn39xhvaSVoJyQzgTaKb13ScnhHxzmc9C3aYoXiD6kt")

# Create API object
api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)


search = "#FreePalestine"
numberOfTweets = 20

for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.retweet()
        print('Retweeted the tweet')
        user = tweet.user
        user.follow()
        print('Followed ' + tweet.user.name)
    except:
        print('Retweet failed')

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

