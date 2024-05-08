
#Importing the requests and json modules
import requests
import json


#This is the URL for the restful API on the CSO website. 
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

#Function to get the json data and store it in variable response
def getall():
    response = requests.get(url)
    return response.json()

#Automatically run the function when the file is opened
if __name__ == "__main__":
    #Crete a .json file called cso.json and store it in the local directory. This section also converts the data received from a dictionary to json format
    with open("cso.json","wt") as fp:
        print(json.dumps(getall()), file = fp)
