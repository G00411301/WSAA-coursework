import requests
import json
from config import config as cfg

#setting up variables for use throughout scriptm valtoreplace is the value that we want to replace ("Andrew"), new val is my name and the filename is the file created when the file is downloanded
valtoreplace = 'G00411301'
newval = 'Michael'
filename = 'JSONdata.json'


#pull in github API key from config file (included in git ignore)
apikey = cfg["githubapi"]
#Url of repo
url = 'https://api.github.com/repos/G00411301/aprivateone'

#Download and generate a new file with the api request data
response = requests.get(url, auth=('token',apikey))
print(response.status_code)
repoJSON = response.json()

#This section creates a new file called filename and dumps the json data into it
with open(filename, 'wt') as fp:
    json.dump(repoJSON, fp, indent = 4)
 
#This code reads in the file and locates the data to be replace
with open(filename,'r') as f:
    data = f.read()
    data = data.replace(valtoreplace, newval)

#This code, replaces the data with the changed data and writes it to the file
with open(filename, 'w') as f:
    f.write(data)

#confiming script has re-written file
print("JSON Data Replaced")

coommiturl = 'https://api.github.com/repos/G00411301/aprivateone/contents/sample.pdf'
commitresponse = requests.get(coommiturl, auth=('token',apikey))
print(commitresponse.status_code)
print(commitresponse)

