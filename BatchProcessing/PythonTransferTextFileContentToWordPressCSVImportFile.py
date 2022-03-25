import os
import os.path
import csv
from datetime import datetime

TESTSourceFiles = '/mnt/e/test/TESTTRANSFER/Content'
TESTDirectory = '/mnt/e/test/TESTTRANSFER/TESTCSVDirect'
TESTWPCSV = 'TESTWPUpload.csv'
TESTOutput = os.path.join(TESTDirectory, TESTWPCSV)

for TESTFile in os.listdir(TESTSourceFiles):
    TESTOSFILEPATH= os.path.join(TESTSourceFiles, TESTFile)
    with open(TESTOSFILEPATH, 'r') as TESTFileContent:
        GenContent=TESTFileContent.readlines()[1:]
        with open(TESTOutput, 'a') as TESTCSVDATAFILE:
            TESTCSVDATAdWriter = csv.writer(TESTCSVDATAFILE, delimiter=',')
            PostID=None
            PostAuthor='1'
            PostDate=datetime.now().replace(microsecond=0).isoformat() + 'Z'
            PostType='post'
            PostStatus='published'
            PostTitle=str(TESTFile[0:-4].replace('', '?'))
            PostSlug=str(PostTitle.replace(' ', '-'))
            PostContent=GenContent
            PostCategory='somecategory'
            PostTags='some, tags'
            PostCustom=None
            def StripLine():
                NewPost=' '.join(PostContent)
                return(NewPost[1:-2].replace('some text to replace', 'substitution text')+' more text at the end of content')
            TESTCSVDATAdWriter.writerow([PostID, PostSlug, PostAuthor, PostDate, PostType, PostStatus, PostTitle, StripLine(), PostCategory, PostTags, PostCustom])
            TESTCSVDATAFILE.close()
        TESTFileContent.close()
