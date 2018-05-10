import sys
import csv
reload(sys)
import operator
sys.setdefaultencoding('utf-8')

reader = csv.reader(open('data.csv', 'rb'), delimiter=',')

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

reader = csv.reader(open('data.csv', 'rb'), delimiter=',')

for i,line in enumerate(reader):
    dataset[line[0]][line[1]] = line[3]

#print(dataset)

reader = csv.reader(open('data.csv', 'rb'), delimiter=',')

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

reader = csv.reader(open('data.csv', 'rb'), delimiter=',')

for i,line in enumerate(reader):
    dataset1[line[1]][line[0]] = line[3]



myData = dict()

myReader = csv.reader(open('myData.csv', 'rb'), delimiter=',')
for i,line in enumerate(myReader):
	myData[line[0]] = dict()

myReader = csv.reader(open('myData.csv', 'rb'), delimiter=',')
for i,line in enumerate(myReader):
	myData[line[0]][line[1]] = int(line[2])


print("READY")

print("myData symptoms vs symptoms and count")
print("dataset1 -> diseases vs symptomps and weight")
print("dataset -> symptoms vs diseases and weight of data.csv")
#x = myData['Dizziness']
#myDict = sorted(x.items(), key=operator.itemgetter(1))
#myDict.reverse()
#print(myDict)

#print(myDict[0][0])

answerr = 0
