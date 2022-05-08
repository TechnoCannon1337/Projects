import os
import requests
import csv
import json
import base64
from datetime import datetime
postsURL = 'https://domainname.com/wp-json/wp/v2/posts'
tagsURL = 'https://domainname.com/wp-json/wp/v2/tags'
catsURL = 'https://domainname.com/wp-json/wp/v2/categories'
user = 'username'
password = '0123 4567 8901 2345 6789 0123'
credentials = user + ':' + password
token = base64.b64encode(credentials.encode())
header = {'Authorization': 'Basic ' + token.decode('utf-8'),
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
post = {
 'status'   : 'publish'
}
wordPressresponse = requests.get(postsURL, headers=header, json=post)
postParser = json.loads(str(wordPressresponse.text))
postSlug = str(postParser[0]['slug'])
postTitle = str(postParser[0]['title'])[13:-1]
postContent = str(postParser[0]['content'])[13:-21]
postExcerpt = str(postParser[0]['excerpt'])[13:-21]
postCats = str(postParser[0]['categories'])[1:-1]#ID numbers
postTags = str(postParser[0]['tags'])[1:-1]#ID numbers
postTagsByName = []
postCatsByName = []
for tag in postTags.split(', '):
    postTagRequest = requests.get(tagsURL+'/'+tag, headers=header)
    tagParser = json.loads(str(postTagRequest.text))
    postTagsByName.append(str(tagParser['name']))
for cat in postCats.split(', '):
    postCatRequest = requests.get(catsURL+'/'+cat, headers=header)
    catParser = json.loads(str(postCatRequest.text))
    postCatsByName.append(str(catParser['name']))
with open('wordPostLog.txt', 'w') as wordPostLogger:
    print(postTitle+'\n\n',postSlug+'\n\n',postExcerpt+'\n\n',str(postCatsByName)+'\n\n',str(postTagsByName)+'\n\n',postContent+'\n\n', file=wordPostLogger)
