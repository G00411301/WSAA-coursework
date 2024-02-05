#The objective of this script is to read in the data from an api at https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m

import requests #import the requests module to connect to the api

#create a variable url to detail the url of the api
#url = "https://api.open-meteo.com/v1/forecast?latitude=53.82&longitude=-9.5&current=temperature_2m,wind_speed_10m"


#create a variable that calls the api and converts the response to json format
#response = requests.get(url).json()

#temp = response['current']['temperature_2m']
#print("The current temperature is", temp, "Degrees Celsius")

#Extra Marks QUestion

# the following script adds the wind direction at 10m to the api parameters and prints it to the screen with the temperature

url2 = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_direction_10m"
response2 = requests.get(url2).json()
print(response2)
temp2 = 

#print(response2)