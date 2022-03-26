import os
import os.path
import csv
import json
import requests
import base64
from datetime import datetime

GitHubDemoSourceFiles = '/mnt/e/test/GitHubDemoTRANSFER/recreationContentTest'
GitHubDemoDirectory = '/mnt/e/test/GitHubDemoTRANSFER/GitHubDemoCSVDirect'
GitHubDemoWPCSV = 'GitHubDemoWPUploadTest.csv'
GitHubDemoOutput = os.path.join(GitHubDemoDirectory, GitHubDemoWPCSV)

for GitHubDemoFile in os.listdir(GitHubDemoSourceFiles):
    GitHubDemoOSFILEPATH= os.path.join(GitHubDemoSourceFiles, GitHubDemoFile)
    with open(GitHubDemoOSFILEPATH, 'r') as GitHubDemoFileContent:
        GenContent=GitHubDemoFileContent.readlines()[1:]
        with open(GitHubDemoOutput, 'a') as GitHubDemoCSVDATAFILE:
            GitHubDemoCSVDATAdWriter = csv.writer(GitHubDemoCSVDATAFILE, delimiter=',')
            PostID=None
            PostAuthor='1'
            PostDate=datetime.now().replace(microsecond=0).isoformat() + 'Z'
            PostType='post'
            PostStatus='publish'
            PostTitle=str(GitHubDemoFile[0:-4].replace('', '?'))
            PostSlug=str(PostTitle.replace(' ', '-'))
            PostContent=GenContent
            PostCategory=['31337']
            PostTags= ['31337', '2600', '143', '247', '365']
            PostCustom=None
            def StripLine():
                NewPost=' '.join(PostContent)
                return(NewPost[1:-2].replace('some text to replace', 'substitution text')+' more text at the end of content')
            GitHubDemoCSVDATAdWriter.writerow([PostID, PostSlug, PostAuthor, PostDate, PostType, PostStatus, PostTitle, StripLine(), PostCategory, PostTags, PostCustom])
            GitHubDemoCSVDATAFILE.close()
            url = 'https://domainName.com/wp-json/wp/v2/posts'
            user = 'UserName'
            password = '0123 4567 8901 2345 6789 0123'
            credentials = user + ':' + password
            token = base64.b64encode(credentials.encode())
            header = {'Authorization': 'Basic ' + token.decode('utf-8'),
                      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
            post = {
                'title': PostTitle,
                'status': PostStatus,
                'content': StripLine(),
                'author': PostAuthor,
                'format': 'standard',
                'slug': PostSlug,
                'tags': PostTags,
                'categories': PostCategory,
                'date_gmt': datetime.now().replace(microsecond=0).isoformat() + 'Z'
            }
            wordPressresponse = requests.post(url, headers=header, json=post)
            with open('wordPresResponseLog.txt', 'a') as wPResponse:
                wPResponse.write(str(wordPressresponse))
        GitHubDemoFileContent.close()
