import os
import requests
import csv
import json
import base64
import math
from datetime import datetime
postsURLdeparture = 'https://domainname.com/wp-json/wp/v2/posts'
tagsURLdeparture = 'https://domainname.com/wp-json/wp/v2/tags'
catsURLdeparture = 'https://domainname.com/wp-json/wp/v2/categories'
departingUser = 'username'
departingPassword = '0123 4567 8901 2345 6789 0123'
departingCredentials = departingUser + ':' + departingPassword
departingToken = base64.b64encode(departingCredentials.encode())
departingHeader = {'Authorization': 'Basic ' + departingToken.decode('utf-8'),
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
departingPostCheck = {
 'status'   : 'publish',
}
departingWordPressresponseCheck = requests.get(postsURLdeparture, headers=departingHeader, json=departingPostCheck)
#totalDepartingPages = departingWordPressresponseCheck.headers['X-WP-TotalPages']
totalDepartingPosts = departingWordPressresponseCheck.headers['X-WP-Total']
#totalDepartingPagesIntegers = int(totalDepartingPages)
totalDepartingAdjustedPages = math.ceil(int(totalDepartingPosts)/5)
#for departingPageCount in range(1,totalDepartingPagesIntegers+1):
for departingPageCount in range(1,totalDepartingAdjustedPages+1):
    departingPageLoad = departingPageCount
    departingPostParams = {
    'per_page' : 5,
    'page' : departingPageLoad
    }
    departingWordPressresponse = requests.get(postsURLdeparture, headers=departingHeader, params=departingPostParams ,json=departingPostCheck)
    departingPostParser = json.loads(str(departingWordPressresponse.text))
    for count,post in enumerate(departingPostParser):
        departingPostSlug = str(departingPostParser[count]['slug'])
        departingPostTitle = str(departingPostParser[count]['title'])[13:-1]
        departingPostContent = str(departingPostParser[count]['content'])[13:-21]
        departingPostExcerpt = str(departingPostParser[count]['excerpt'])[13:-21]
        departingPostCats = str(departingPostParser[count]['categories'])[1:-1]#ID numbers
        departingPostTags = str(departingPostParser[count]['tags'])[1:-1]#ID numbers
        departingPostTagsByName = []
        departingPostCatsByName = []
        for tag in departingPostTags.split(', '):
            departingPostTagRequest = requests.get(tagsURLdeparture+'/'+tag, headers=departingHeader)
            departingTagParser = json.loads(str(departingPostTagRequest.text))
            departingPostTagsByName.append(str(departingTagParser['name']))
        for cat in departingPostCats.split(', '):
            departingPostCatRequest = requests.get(catsURLdeparture+'/'+cat, headers=departingHeader)
            departingCatParser = json.loads(str(departingPostCatRequest.text))
            departingPostCatsByName.append(str(departingCatParser['name']))
        with open('wordPostLog.txt', 'a') as worddepartingPostLogger:
            print(str(departingPageLoad)+' of '+str(totalDepartingAdjustedPages)+'\n\n',departingPostTitle+'\n\n',str(departingPostCatsByName)+'\n\n',str(departingPostTagsByName)+'\n\n', file=worddepartingPostLogger)
        postsURLarrival = 'https://domainname.com/wp-json/wp/v2/posts'
        tagsURLarrival = 'https://domainname.com/wp-json/wp/v2/tags'
        catsURLarrival = 'https://domainname.com/wp-json/wp/v2/categories'
        arrivingUser = 'username'
        arrivingPassword = '0123 4567 8901 2345 6789 0123'
        arrivingCredentials = arrivingUser + ':' + arrivingPassword
        arrivingToken = base64.b64encode(arrivingCredentials.encode())
        arrivingHeader = {'Authorization': 'Basic ' + arrivingToken.decode('utf-8'),
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
        arrivingPostCats= departingPostCatsByName
        arrivingPostTags= departingPostTagsByName
        arrivingNewTagArray = []
        arrivingNewCatArray= []
        for cat in arrivingPostCats:
            arrivingJsonCatFormat= {'name': cat}
            wordPressRESTAPIarrivingPostNewCatRequest = requests.post(catsURLarrival, headers=arrivingHeader, json=arrivingJsonCatFormat)
            arrivingCatParser = json.loads(str(wordPressRESTAPIarrivingPostNewCatRequest.text))
            arrivingCatParserStatusCode = json.loads(str(wordPressRESTAPIarrivingPostNewCatRequest.status_code))
            if arrivingCatParserStatusCode == 400 and str(arrivingCatParser['code']) == 'term_exists':
                arrivingNewCatArray.append(str(arrivingCatParser['data']['term_id']))
            elif arrivingCatParserStatusCode == 201:
                arrivingNewCatArray.append(str(arrivingCatParser['id']))
            with open('arrivingWordPressNewCatResponseLog.txt', 'a') as arrivingwPNewCatResponse:
                arrivingwPNewCatResponse.write(str(arrivingCatParser)+'\n\n')
        with open('arrivingCatParserLog.txt', 'a') as wPNewarrivingCatParserResponse:
            wPNewarrivingCatParserResponse.write(str(arrivingNewCatArray))
        for tag in arrivingPostTags:
            arrivingJsonTagFormat= {'name': tag}
            wordPressRESTAPIarrivingPostNewTagRequest = requests.post(tagsURLarrival, headers=arrivingHeader, json=arrivingJsonTagFormat)
            arrivingTagParser = json.loads(str(wordPressRESTAPIarrivingPostNewTagRequest.text))
            arrivingTagParserStatusCode = json.loads(str(wordPressRESTAPIarrivingPostNewTagRequest.status_code))
            if arrivingTagParserStatusCode == 400 and str(arrivingTagParser['code']) == 'term_exists':
                arrivingNewTagArray.append(str(arrivingTagParser['data']['term_id']))
            elif arrivingTagParserStatusCode == 201:
                arrivingNewTagArray.append(str(arrivingTagParser['id']))
            with open('arrivingWordPressNewTagResponseLog.txt', 'a') as arrivingwPNewTagResponse:
                arrivingwPNewTagResponse.write(str(arrivingTagParser)+'\n\n')
        with open('arrivingTagParserLog.txt', 'a') as wPNewarrivingTagParserResponse:
            wPNewarrivingTagParserResponse.write(str(arrivingNewTagArray))
        arrivingPost = {
         'title'    : departingPostTitle,
         'status'   : 'draft',
         'content'  : departingPostContent,
         'excerpt'  : departingPostExcerpt,
         'categories': arrivingNewCatArray,
         'date_gmt' : datetime.now().replace(microsecond=0).isoformat() + 'Z',
         'format' : 'standard',
         'tags' : arrivingNewTagArray,
         'author' : '1'
        }
        arrivingWordPressresponse = requests.post(postsURLarrival, headers=arrivingHeader, json=arrivingPost)
        with open('arrivingWordPresResponseLog.txt', 'a') as arrivingwPResponse:
            arrivingwPResponse.write(str(arrivingWordPressresponse.text))
