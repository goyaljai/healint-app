from bs4 import BeautifulSoup as bs
import re
from requests import get
import csv
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

reader = csv.reader(open('data.csv', 'rb'), delimiter=',')

symptoms = set()

for i,line in enumerate(reader):
	symptoms.add(line[0])

csvv = open("shgcrip.csv", "w")
csvvv = csv.writer(csvv)


def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7F]+','', text)

def get_soup(url):
  	raw = remove_non_ascii(get(url).content)
  	soup = bs(raw)
  	return soup.select("#MainTxt")[0].select('.ds-single')[0].text.strip()

def lookup(word):
    base_url  = "http://www.thefreedictionary.com/"
    query_url = base_url + word
    return get_soup(query_url)


def remove_non_ascii1(text):
    return re.sub(r'[^\x00-\x7F]+','', text)

def get_soup1(url):
  	raw = remove_non_ascii1(get(url).content)
  	soup = bs(raw)
  	divTag = soup.find_all("div", {"id": "Definition"})

  	for tag in divTag:
  	    tdTags = tag.find_all("div", {"class": "runseg"})
  	    for tag in tdTags:
  	        return tag.text.strip().split(".")[0]


def lookup1(word):
    base_url  = "http://medical-dictionary.thefreedictionary.com/"
    query_url = base_url + word
    return get_soup1(query_url)


def remove_non_ascii2(text):
    return re.sub(r'[^\x00-\x7F]+','', text)

def get_soup2(url):
    raw = remove_non_ascii2(get(url).content)
    soup = bs(raw)
    divTag = soup.find_all("div", {"id": "Definition"})

    for tag in divTag:
        tdTags = tag.find_all("div")
        for tag in tdTags:
            return tag.text.strip().split(".")[0]


def lookup2(word):
    base_url  = "http://medical-dictionary.thefreedictionary.com/"
    query_url = base_url + word
    return get_soup2(query_url)

#print(lookup1("Susac Syndrome".split(",")[0]))

symptoms = list(symptoms)
i=1
jaii = 0
for item in symptoms:
  print(item)
  i=i+1
  try:
    jj = lookup(item.split(",")[0])
    csvvv.writerow([item,jj])
 #   print(lookup(item.split(",")[0]))
    print("here1")
    while(jj==None or jj==""):
      print("hi")
      csvvv.writerow([item,jj])
  except:
    print("here2")
    try:
      jaii=0
      jjjj=lookup1(item.split(",")[0])
      if(jjjj!=None):
        csvvv.writerow([item,jjjj])
      else:
        jjjj=lookup2(item.split(",")[0])
        csvvv.writerow([item,jjjj])
    except Exception, e:
      jaii=0