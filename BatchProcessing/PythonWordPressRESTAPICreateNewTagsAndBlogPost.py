import os
import os.path
import csv
import json
import requests
import base64
from datetime import datetime
      
postsURL = 'https://domainName.com/wp-json/wp/v2/posts'
tagsURL = 'https://domainName.com/wp-json/wp/v2/tags'
user = 'username'
password = '0123 4567 8901 2345 6789 0123'
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8'),
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

PostTags= ['recreation', 'fun', 'activities', 'games', 'sports', 'leisure', 'entertainment', 'extracurricular', 'extracurricular activities', 'pastime', 'pastime activity', 'pastime activity', 'extracurricular activity', 'free time', 'free time activity', 'free time activities', 'hobby', 'hobbies', 'recreation activity', 'parks and recreation', 'recreaction activities', 'gaming', 'outdoors', 'outdoor activity', 'outdoor activities', 'r&r', 'r and r', 'family fun', 'amusement', 'enjoyment', 'pleasure', 'recreational activity', 'recreational activities', 'play', 'playtime', 'outdoor recreation', 'leisure time', 'rest and recreation', 'rest and relaxation', 'excitment']

newTagArray = []

for tag in PostTags:
    jsonTagFormat= {'name': tag}
    wordPressRESTAPIPostNewTagRequest = requests.post(tagsURL, headers=header, json=jsonTagFormat)
    tagParser = json.loads(str(wordPressRESTAPIPostNewTagRequest.text))
    tagParserStatusCode = json.loads(str(wordPressRESTAPIPostNewTagRequest.status_code))
    if tagParserStatusCode == 400 and str(tagParser['code']) == 'term_exists':
        newTagArray.append(str(tagParser['data']['term_id']))
    elif tagParserStatusCode == 201:
        newTagArray.append(str(tagParser['id']))
    with open('wordPressNewTagResponseLog.txt', 'a') as wPNewTagResponse:
        wPNewTagResponse.write(str(tagParser)+'\n\n')
with open('tagParserLog.txt', 'a') as wPNewTagParserResponse:
    wPNewTagParserResponse.write(str(newTagArray))

post = {
    'title': 'test',
    'status': 'publish',
    'content': 'testing testing 123',
    'author': '1',
    'format': 'standard',
    'slug': 'test-testing-123',
    'tags': newTagArray,
    'categories': '2',
    'date_gmt': datetime.now().replace(microsecond=0).isoformat() + 'Z'
}


wordPressresponse = requests.post(postsURL, headers=header, json=post)
with open('wordPresResponseLog.txt', 'a') as wPResponse:
    wPResponse.write(str(wordPressresponse))
