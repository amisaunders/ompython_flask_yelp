# weather.py
# -*- coding: utf-8 -*-
local_encoding = 'cp850' 

import forecastio
from geopy.geocoders import Nominatim
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


def get_weather(address):
	api_key = os.environ['WEATHER_API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	latitude = location.latitude
	longitude = location.longitude
	forecast = forecastio.load_forecast(api_key, latitude, longitude).currently()
	summary = forecast.summary
	temperature = forecast.temperature
	return "{} and {}° in {}".format(summary, temperature, address)
