import os
import json
import requests
import base64

url = 'https://domainName.com/wp-json/wp/v2/posts'

user = 'UserName'
password = '0123 4567 8901 2345 6789 0123'

credentials = user + ':' + password

token = base64.b64encode(credentials.encode())

header = {'Authorization': 'Basic ' + token.decode('utf-8'),
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}

post = {
    'date': '2022-03-23T10:00:00',
    'title': 'testing',
    'content': 'testing testing 123',
    'status': 'publish'
}

wordPressresponse = requests.post(url,headers=header, json=post)
with open('wordPresResponseLog.txt', 'w') as wPResponse:
    wPResponse.write(str(wordPressresponse))
