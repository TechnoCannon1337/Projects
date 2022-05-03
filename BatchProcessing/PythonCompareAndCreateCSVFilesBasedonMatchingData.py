import os
import os.path
import csv

with open('careerMainLoopFile.csv', 'r') as careerManLoop:
    findsource1URL = csv.reader(careerManLoop)
    for row in findsource1URL:
        careerManSourceTitle = row[0]
        source1URL = row[1]
        source2URL = row[2]
        with open('allergic.csv', 'r') as allergicResponse:
            allergicReaction = csv.reader(allergicResponse)
            for row in allergicReaction:
                allergyTitle = row[0]
                allergySymptom = row[1]
                with open('allergyDiagnosis.csv', 'a') as allergyDiagnosticExam:
                    allergyDiagnosticResults = csv.writer(allergyDiagnosticExam)
                    if careerManSourceTitle == allergyTitle and allergySymptom == 'sourceEntreeshortDescription':
                        allergyDiagnosticResults.writerow([allergyTitle, allergySymptom, source1URL])
                    elif careerManSourceTitle == allergyTitle and allergySymptom == 'source2Appetizer':
                        allergyDiagnosticResults.writerow([allergyTitle, allergySymptom, source2URL])
