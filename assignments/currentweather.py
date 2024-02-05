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

#URL to API
url2 = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_direction_10m"

#Get the API response from the server and convert to json
response2 = requests.get(url2).json()

#print the response to identify data points
#print(response2)

#create a variable for temperature and wind direction
temp2 = response2['current']['temperature_2m']
x = response2['current']['wind_direction_10m']



#print temperature and one direction to the terminal
print("The current temperature is", temp2, "Degrees Celsius")
#print("The current wind direction at 10m is", winddirec, "Degre")

#Use an if and elif statement to convert the degress that the API reports wind direction in to a verbal wind direction
if 0 <= x <= 45:
    print("The current wind direction at 10 m is: North/North East")
elif 46 <= x <= 90:
    print("The current wind direction at 10 m is: North East/East")
elif 91 <= x <= 135:
    print("The current wind direction at 10 m is: East/South East")
elif 136 <= x <= 180:
    print("The current wind direction at 10 m is: South East/South")
elif 181 <= x <= 225:
    print("The current wind direction at 10 m is: South/South West")
elif 226 <= x <= 270:
    print("The current wind direction at 10 m is: South West/West")
elif 271 <= x <= 315:
    print("The current wind direction at 10 m is: West/North West")
elif 316 <= x <= 360:
    print("The current wind direction at 10 m is: North West/North")