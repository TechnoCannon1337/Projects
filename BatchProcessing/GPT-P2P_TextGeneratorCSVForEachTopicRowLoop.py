#This program loops through a csv file containing several rows of prompts and topic names before feeding the prompts designated
#on the first column of each row to the OpenAI GPT-3 Model, which then returns the results in the form of a text file named 
#according to the topic names designated on the second column of each row.
import os
import openai
import os.path
import csv
openai.api_key = 'OPENAI_API_KEY'
with open('GPTP2PInputFile.csv', 'r') as GPTP2PPrompts:
    GPTP2PReader = csv.reader(GPTP2PPrompts)
    for row in GPTP2PReader:
        response = openai.Completion.create(
          engine="text-davinci-001",
          prompt=row[0],
          temperature=0.9,
          max_tokens=1500,
          top_p=1,
          echo=True,
          frequency_penalty=0.2,
          presence_penalty=0
        )
        GPTP2PPath = '/mnt/e/GPTP2POutputFolder'
        GPTP2PFileName = row[1]+'.txt'
        GPTP2PExport = os.path.join(GPTP2PPath, GPTP2PFileName)
        with open(GPTP2PExport, 'w') as GPTP2PAnswer:
            GPTP2PWriter = csv.writer(GPTP2PAnswer)
            GPTP2PWriter.writerow([response.choices[0].text])
