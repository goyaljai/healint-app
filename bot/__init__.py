#import sys
import csv
#reload(sys)
import operator
#sys.setdefaultencoding('utf-8')

reader = csv.reader(open('data.csv', 'r'), delimiter=',')

diseases = set()
symptoms = set()

for i,line in enumerate(reader):
	diseases.add(line[1])
	symptoms.add(line[0])

diseases = list(diseases)

symptoms = list(symptoms)

dataset = dict()

for i in range(len(symptoms)):
	dataset[symptoms[i]] = dict()

reader = csv.reader(open('data.csv', 'r'), delimiter=',')

for i,line in enumerate(reader):
    dataset[line[0]][line[1]] = line[3]

#print(dataset)

reader = csv.reader(open('data.csv', 'r'), delimiter=',')

diseases = set()
symptoms = set()

for i,line in enumerate(reader):
	diseases.add(line[1])
	symptoms.add(line[0])

diseases = list(diseases)
symptoms = list(symptoms)

dataset1 = dict()

for i in range(len(diseases)):
	dataset1[diseases[i]] = dict()

reader = csv.reader(open('data.csv', 'r'), delimiter=',')

for i,line in enumerate(reader):
    dataset1[line[1]][line[0]] = line[3]



myData = dict()

myReader = csv.reader(open('myData.csv', 'r'), delimiter=',')
for i,line in enumerate(myReader):
	myData[line[0]] = dict()

myReader = csv.reader(open('myData.csv', 'r'), delimiter=',')
for i,line in enumerate(myReader):
	myData[line[0]][line[1]] = int(line[2])

answerr = 0
