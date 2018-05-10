import duckduckgo


import csv

reader = csv.reader(open('data.csv', 'rb'), delimiter=',')

symptoms = set()
finalLst = list()
for i,line in enumerate(reader):
	symptoms.add(line[0])

i=1
for string in list(symptoms):
    print("iteration "+str(i))
    i+=1
    string = string.encode('utf-8')
    lst = list()
    lst.append(string)
    string = string.split(",")[0]
    answer1=""
    answer2=""
    answer3=""
    answer=""
    try:
        answer1 = duckduckgo.query(string).abstract.text
    except Exception as e:
        pass

    try:
        answer2 = duckduckgo.query(string).results[0].text
    except Exception as e:
        pass
    try:
        answer3 = duckduckgo.query(string).related[0].text
    except Exception as e:
        pass
    #answer = answer.strip().

    if(len(answer1)<2):
        if(len(answer2)<2):
            if(len(answer3)<2):
                answer = "..."
            else:
                answer = answer3
        else:
            answer = answer2
    else:
        answer = answer1
    answer = answer.split(".")[0]+"."
    lst.append(answer)
    finalLst.append(lst)

f = open('123meanings.csv', 'w')
with f:
    writer = csv.writer(f)
    for lst in finalLst:
        writer.writerow(lst)
