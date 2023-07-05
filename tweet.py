from requests_oauthlib import OAuth1Session
import os
import json
import time
from datetime import datetime

def tweet():

    access_token = 'YOUR_ACCESS_TOKEN'
    access_token_secret = 'YOUR_ACCESS_TOKEN_SECRET'

    consumer_key = "YOUR_CONSUMER_KEY"
    consumer_secret = "YOUR_CONSUMER_KEY_SECRET"

    # Be sure to add replace the text of the with the text you wish to Tweet
    payload = {"text": "There is a water leak in the basement! Please delete the post when you see it. If you don't do so in 30 min, you'll be notified again."}

    now = datetime.now()
    time1 = now.strftime("%H:%M:%S")
    payload["text"] += " Time: " + time1

    # Make the request
    oauth = OAuth1Session(
        consumer_key,
        client_secret=consumer_secret,
        resource_owner_key=access_token,
        resource_owner_secret=access_token_secret,
    )

    # Making the request
    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))


    # Saving the response as JSON
    json_response = response.json()
    tweet_already_exists = len(json_response["data"]) > 0

    # if the first post is not deleted after 30 min, then post a second one
    # feel free to change the time from 30 min to something else
    if tweet_already_exists:
        print("The first tweet already exists")
        print("Waiting for 30 minutes before posting the second tweet.")
        time.sleep(int(1*60))

        new_text = "Warning: Your second reminder about the leak in the basement! Please, delete the post once you see it."
        payload = {"text": new_text}

        response = oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )

        if response.status_code != 201:
            raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))

        print("Second tweet posted successfully!")
    else:
        print("First tweet posted successfully!")
        print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))

tweet()
