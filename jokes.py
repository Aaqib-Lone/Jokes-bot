from logging import exception
import tweepy
import datetime
import time
import apikeyJoke
import requests

while True:
	url = "https://humor-jokes-and-memes.p.rapidapi.com/jokes/random"

	querystring = {"api-key":"undefined","max-length":"200","include-tags":"one_liner","min-rating":"7","exclude-tags":"nsfw","keywords":"rocket"}

	headers = {
		"X-RapidAPI-Host": "host",
		"X-RapidAPI-Key": "apikey"
	}
	
	response = requests.request("GET", url, headers=headers, params=querystring).json()

	# print(response['joke'])
	joke=response['joke']
	
	api_key=apikeyJoke.API_KEY
	api_key_secret=apikeyJoke.API_KEY_SECRET
	access_token=apikeyJoke.ACCESS_TOKEN
	access_token_secret=apikeyJoke.ACCESS_TOKEN_SECRET

	auth= tweepy.OAuthHandler(api_key, api_key_secret)
	auth.set_access_token(access_token, access_token_secret)

	api=tweepy.API(auth)

	api.update_status(joke+"\n"+ str(datetime.datetime.now()))
	print("Tweet sent...")
	time.sleep(1600)