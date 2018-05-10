import csv
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk import pos_tag, word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize
import sys
import math
from django.contrib.auth.models import User
from bot import *
import operator
from bot.models import Disease
reload(sys)
sys.setdefaultencoding("utf-8")
#
#
# diseasePrediction = dict()
#
#
# for item in diseases:
# 	diseasePrediction[item] = 0
#
# symptomsPruned = dict()
#
# for item in symptoms:
# 	symptomsPruned[item] = 0
#
#
# def func1(string,mainSet,thresh_val,index,uid):
# 	#string is already stemmed and been founded in the dataset
# 	###print(string)
# 	diseaseSet = set()
# 	global diseasePrediction
# 	global symptomsPruned
# 	diseaseDict = dict()
#
# 	diseaseDict = dataset[string]
#
# 	for key,val in diseaseDict.items():
# 		diseaseSet.add(key)
#
# 	mainSet = mainSet.intersection(diseaseSet) # this may give error
#
# 	iterr = list(mainSet)
#
# 	jai = 0
# 	##print(iterr)
# 	for i in range(len(iterr)):
# 		jai=jai+1
# 		#diss = Disease.objects.filter(user=user)
# 		vall = diseasePrediction[iterr[i]]
# 		vall=vall+1
# 		diseasePrediction[iterr[i]]=vall
#
# 	###print("hooooooooooooooooooooooooooooo"+str(diseasePrediction['Anemia']))
# 	answerDisease = sorted(diseasePrediction.items(), key=operator.itemgetter(1))
# 	answerDisease.reverse()
# 	finalAnswer=set()
# 	##print("0000")
# 	##print(answerDisease)
# 	for i in range(len(answerDisease)):
# 		if(diseasePrediction[answerDisease[0][0]]>5):
# 			finalAnswer.add(answerDisease[i][0])
# 			if(len(finalAnswer)==5):
# 				return finalAnswer
# 		else:
# 			break
#
#
#
# 	###print(diseasePrediction)
#
# 	lst = list(mainSet)
#
# 	x = myData[string]
# 	myDict = sorted(x.items(), key=operator.itemgetter(1))
# 	myDict.reverse()
#
# 	toBeReturned = set()
#
# 	for i in range(len(myDict)):
# 		if(len(toBeReturned)<10):
# 			if(symptomsPruned[myDict[i][0]]==0):
# 				toBeReturned.add(myDict[i][0])
# 				symptomsPruned[myDict[i][0]]=1
#
# 	if(index==thresh_val):
# 		return toBeReturned
# 	else:
# 		return mainSet
#
#
# def stemmer(string,uid):
#
# 	mainSet = set()
# 	wnl = WordNetLemmatizer()
# 	stop_words = set(stopwords.words('english'))
# 	word_tokens = word_tokenize(string)
# 	filtered_sentence = [w for w in word_tokens if not w in stop_words]
#
# 	string = ""
#
# 	for i in range(len(filtered_sentence)):
# 		string = string + filtered_sentence[i]
# 		string = string + " "
#
# 	newString = str()
# 	for word, tag in pos_tag(word_tokenize(string)):
# 		wntag = tag[0].lower()
# 		wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
# 		lemma = wnl.lemmatize(word, wntag) if wntag else word
# 		newString = newString + lemma
# 		newString = newString + " "
#
# 	prediction = set()
#
# 	ps = PorterStemmer()
#
# 	for word in newString.split():
# 		for i in range(len(symptoms)):
#
# 			tokenlist = word_tokenize(symptoms[i])
# 			for j in range(len(tokenlist)):
# 				##print("symptoms[i]")
# 				##print(ps.stem(word))
# 				##print(ps.stem(tokenlist[j]))
# 				if(ps.stem(word) in ps.stem(tokenlist[j])):
#
# 					prediction.add(symptoms[i])
#
# 	prediction = list(prediction)
#
# 	##print(prediction)
# 	mainSet = set(diseases)
# 	for i in range(len(prediction)):
# 		mainSet = func1(prediction[i],set(mainSet),len(prediction)-1,i,uid)
#
# 	return mainSet


diseaseSet = set(diseases)
preDiseases = dict()
hmap_symptoms = dict()
meanings = dict()
global jaiii
jaiii=0

def preComputeDiseases():

	reader = csv.reader(open('meanings.csv', 'rb'), delimiter=',')
	for i,line in enumerate(reader):
		meanings[line[0]] = line[1]

	for disease in diseases:
		if(disease=='Dry Eye Syndromes'):
			print("999999999999999999999999999999999999999999")
		preDiseases[disease]=0

def preComputeSymptoms():

	for symptom in symptoms:
		hmap_symptoms[symptom]=0

preComputeDiseases()
preComputeSymptoms()

def getDiseases(symptom):
	diseaseDict = dict()

	diseaseDict = dataset[symptom]
	count=0

	#print(len(preDiseases))

	for key in sorted(diseaseDict.items(), key=operator.itemgetter(1),reverse=True):
		count+=1
		if(count==20):
			break
		#tempDiseaseSet.add(key)
		preDiseases[str(key[0])]+=1
		print(str(key[0]))
		print(preDiseases[str(key[0])])

def get_symptoms(string,uid):
	global jaiii
	hmap_symptoms
	#print(jaiii)
	jaiii+=1
	#preComputeDiseases()
	hmap_symptoms[string]=-100000000
	mainset = set()
	lemmatizer = WordNetLemmatizer()
	stop_words = set(stopwords.words('english'))
	word_tokens = word_tokenize(string)
	filtered_sentence = [w for w in word_tokens if not w in stop_words]

	string = ""

	for i in range(len(filtered_sentence)):
		string = string + filtered_sentence[i]
		string = string + " "

	newString = str()
	for word, tag in pos_tag(word_tokenize(string)):
		wntag = tag[0].lower()
		wntag = wntag if wntag in ['a', 'r', 'n', 'v'] else None
		lemma = lemmatizer.lemmatize(word, wntag) if wntag else word
		newString = newString + lemma
		newString = newString + " "

        prediction = set()

	ps = PorterStemmer()

	for word in newString.split():
		for i in range(len(symptoms)):

			tokenlist = word_tokenize(symptoms[i])
			for j in range(len(tokenlist)):
				##print("symptoms[i]")
				##print(ps.stem(word))
				##print(ps.stem(tokenlist[j]))
				if(ps.stem(word) in ps.stem(tokenlist[j])):
					prediction.add(symptoms[i])

	predicted_symptoms = list(prediction)

	for symptom in predicted_symptoms:
		getDiseases(symptom)
		symptom_data = dict()
		count = 0
		symptom_data = myData[symptom]
		for key in sorted(symptom_data.items(), key=operator.itemgetter(1),reverse=True):
			#print(key)
			hmap_symptoms[key[0]]+=int(key[1])
			count+=1
			if(count==20):
				break


	#print(hmap_symptoms)

	final_symptoms_list = list()

	count=0
	for final_symptom in sorted(hmap_symptoms.items(), key=operator.itemgetter(1),reverse=True):
		count+=1
		final_symptoms_list.append({"symptom":final_symptom[0],"meaning":meanings[final_symptom[0]]})
		hmap_symptoms[final_symptom[0]]=hmap_symptoms[final_symptom[0]]//2
		if(count==10):
			break;

	return final_symptoms_list


def get_diseases():
	count=0
	answer = list()
	for disease in sorted(preDiseases.items(), key=operator.itemgetter(1),reverse=True):
		answer.append(disease[0])
		count+=1
		if(count==6):
			break

	return answer


def init(string):

	analyser = SentimentIntensityAnalyzer()
	snt = analyser.polarity_scores(string)
	flag=0
	if(snt['neg'] < snt['pos']):
		flag=1
	if(snt['neg'] < snt['neu']):
		flag=2
	if(snt['neg'] < abs(snt['compound'])):
		flag=1

	if(flag==1):
		return "Thats Great, Good to hear!! Now Coming back to your Symptoms!! Lets Discuss!!"

	if(flag==2):
		return "Ok!! Now Coming back to your Symptoms!! Lets Discuss!!"

	if(flag==0):
		return "Ohh!! According to my Research, Playing Music and Eating Good Food will make you happy.. Now Coming back to your Symptoms!! Lets Discuss!!"
