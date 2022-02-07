import os.path
import csv
with open('GPTPromptList.csv', 'r') as GPTP2PPrompts:
    GPTP2PReader = csv.reader(GPTP2PPrompts)
    for row in GPTP2PReader:
        GPTP2PPath = '/mnt/e/PythonTest/GPTP2PFolder'
        GPTP2PFile = row[2]+'.csv'
        GPTP2POutput = os.path.join(GPTP2PPath, GPTP2PFile)
        with open(GPTP2POutput, 'w') as GPTP2PResponse:
            GPTP2PWriter = csv.writer(GPTP2PResponse)
            GPTP2PWriter.writerow([row[0]])
