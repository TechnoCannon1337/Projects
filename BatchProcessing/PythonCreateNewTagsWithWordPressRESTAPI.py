import os
import os.path
import csv
import json
import requests
import base64
from datetime import datetime

tagsURL = 'https://domainName.com/wp-json/wp/v2/tags'
user = 'username'
password = '0123 4567 8901 2345 6789 0123'
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8'),
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

PostTags= ['recreation', 'fun', 'activities']


for tag in PostTags:
    jsonTagFormat= {'name': tag}
    wordPressRESTAPIPostNewTagRequest = requests.post(tagsURL, headers=header, json=jsonTagFormat)
    with open('wordPressTagResponseLog.txt', 'a') as wPTagResponse:
        wPTagResponse.write(str(wordPressRESTAPIPostNewTagRequest))
