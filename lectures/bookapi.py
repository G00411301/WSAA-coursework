import json
import requests

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getallbooks():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    print(getallbooks())
