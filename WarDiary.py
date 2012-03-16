# Word Frequency Analysis for Afghan War Diary, 2004-2010
# 
# 
# Siamak Faridani 
# Revised 3/16/2012
#
#
# For the Poetry & Data project 
# 
# Project page :http://automation.berkeley.edu/open-poem/
# Dataset: http://mirror.wikileaks.info/wiki/Afghan_War_Diary,_2004-2010/



import csv
import time
import re

dataset = 'data/afg.csv' #Change this to point to your own text file

def sortedDictValues(adict,i):
	FreqWriter = csv.writer(open('wordFreq.csv', 'w'), delimiter=',', quotechar='"')
	f = open('wordFreq.csv', 'w')
	for wordPair in adict:
		myRow = ''.join([str(wordPair), ",", str(adict[wordPair]),"\n"])
		f.write(myRow)
	return
	f.close()
	

start = time.clock()
print "Starting..."
TextReader = open(dataset, 'rb')

wordCounts = {}
rowCounter = 0
documents = []
myText = ""
for row in TextReader:
	rowCounter = rowCounter + 1
	myText = ''.join(row)
	DocWords =myText.split(" ")
	if rowCounter%100 == 0:
		print "Processing line: ", rowCounter
	DocWordsCleaned = ""


	for word in DocWords:
		#rules for removing punctuation
		p = re.compile('[^a-zA-Z]+')
		word = p.sub(' ', word)
		DocWordsCleaned = "".join([DocWordsCleaned, " ", word])
	DocWords = DocWordsCleaned.split(" ")

	for word in DocWords:
		#Counting 
		if word.lower() in wordCounts:
			wordCounts[word.lower()] = wordCounts[word.lower()]+1
		else:
			wordCounts[word.lower()] =1

sortedDictValues(wordCounts, rowCounter)
elapsed = (time.clock() - start)
print elapsed


