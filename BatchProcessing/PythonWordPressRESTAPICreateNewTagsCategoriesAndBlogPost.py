import os
import os.path
import csv
import json
import requests
import base64
from datetime import datetime

postsURL = 'https://domainName.com/wp-json/wp/v2/posts'
tagsURL = 'https://domainName.com/wp-json/wp/v2/tags'
catsURL = 'https://domainName.com/wp-json/wp/v2/categories'
user = 'username'
password = '0123 4567 8901 2345 6789 0123'
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8'),
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

PostTags= ['IT Manager', 'Software Engineer']
newTagArray = []
PostCats= ['Information Technology', 'Software Development']
newCatArray= ['526']

for cat in PostCats:
    jsonCatFormat= {'name': cat,
                    'parent': 526}
    wordPressRESTAPIPostNewCatRequest = requests.post(catsURL, headers=header, json=jsonCatFormat)
    catParser = json.loads(str(wordPressRESTAPIPostNewCatRequest.text))
    catParserStatusCode = json.loads(str(wordPressRESTAPIPostNewCatRequest.status_code))
    if catParserStatusCode == 400 and str(catParser['code']) == 'term_exists':
        newCatArray.append(str(catParser['data']['term_id']))
    elif catParserStatusCode == 201:
        newCatArray.append(str(catParser['id']))
    with open('wordPressNewCatResponseLog.txt', 'a') as wPNewCatResponse:
        wPNewCatResponse.write(str(catParser)+'\n\n')
with open('catParserLog.txt', 'a') as wPNewCatParserResponse:
    wPNewCatParserResponse.write(str(newCatArray))

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
    'categories': newCatArray,
    'date_gmt': datetime.now().replace(microsecond=0).isoformat() + 'Z'
}


wordPressresponse = requests.post(postsURL, headers=header, json=post)
with open('wordPresResponseLog.txt', 'a') as wPResponse:
    wPResponse.write(str(wordPressresponse))
