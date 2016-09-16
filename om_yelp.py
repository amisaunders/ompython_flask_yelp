from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os 
from dotenv import load_dotenv, find_dotenv
from operator import itemgetter

# city = "San Mateo"
# term = "food"

# define function to display 
# top 3 spots in a given city for a given search term

def top_spots(address):
	auth = Oauth1Authenticator(
		consumer_key=os.environ['CONSUMER_KEY'],
		consumer_secret=os.environ['CONSUMER_SECRET'],
		token=os.environ['TOKEN'],
		token_secret=os.environ['TOKEN_SECRET']
		)

	client = Client(auth)

	params = {
	'term': 'food',
	'lang': 'en'
	}

	response = client.search(address, **params)
	
	# very common structure, start an empty list and fill it
	responses_list = []

	# iterate in for loop, append each business until list is full
	for business in response.businesses:
		# my solution was to return a tuple
		tuple1 = (business.name, business.rating, business.phone)

		# mattan's solution was to append a dictionary
		# dict1 = ({ name : business.name, 
		# 			rating : business.rating,
		# 			phone : business.phone 
		# })

		# append the list until loop is done and it is full
		responses_list.append(tuple1)

		businesses_by_ratings = sorted(responses_list,key=itemgetter(1))[::-1]

	# return the full list
	return businesses_by_ratings

# # call the function
# for top_spot in top_spots(city, term):
# 	# add exception to formatting if phone is None
# 	if top_spot[2] == None:
# 		print("{} -- rating: {}, phone: {}"
# 			.format(top_spot[0], top_spot[1], top_spot[2]))  
# 	# format phone number as 650-000-0000 if not None
# 	else: 
# 		print("{} -- rating: {}, phone: {}-{}-{}"
# 			.format(top_spot[0], top_spot[1], top_spot[2][0:3], top_spot[2][3:6], top_spot[2][6:]))  
# 		# .format(top_spot[0], top_spot[1], top_spot[2][0:3])) if phone wasn't 'NoneType' would work


