'''
gasChecker.py

Welcome to this app called gasChecker. This application was
designed to tell you how much money you would spend on gas depending
on how far you want to drive, what the average miles per gallon your car
spends, and the average prices for gas in your area.

This was inspired by the DoorDash app because I wanted to see how much profit
I was truly making every time I had to go a certain amount of miles to deliver
an order.

In order for the script to work you will need to install geopy, which will convert
your address into latitude and longitude points for the gas data API to work.

Special thanks to mygasfeed.com for the API data on gas prices.

#Created by Ennis Machta - June 18, 2018
'''

import urllib.request
from geopy.geocoders import Nominatim
import json

#Create the latitude and longitude
#points from the address provided
geolocator = Nominatim()
address = input("Enter your address: ")
location = geolocator.geocode(address)

#Create the URL for the API
url = "http://api.mygasfeed.com/stations/radius/" + str(location.latitude) + "/" + str(location.longitude) + "/1/reg/price/f0bwhhv4jn.json"

#Read the content from the URL and interpret the API (JSON)
response = urllib.request.urlopen(url)
data = response.read().decode()
jsondata = json.loads(data)

#Create the average price of gas
avgprice = float(jsondata["stations"][int(len(jsondata["stations"])/2)]["reg_price"])

mpg = float(input("Enter your miles per gallon of your vehicle: "))
distance = float(input("Enter the miles you are going to travel: "))

#Final result on how much money is spent
result = avgprice * distance / mpg

print("===============================================")
print('\n\n\n\n')
print("The average price of gas in your area is: ${:.2f}".format(avgprice))
print("The amount you will spend is: ${:.2f}".format(result))
