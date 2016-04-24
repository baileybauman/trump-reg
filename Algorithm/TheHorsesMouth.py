from textblob import TextBlob
from xlrd import open_workbook
from collections import Counter
import random
from random import randrange
import re
import json
from nltk.corpus import treebank

class Arm(object):
    def __init__(self, id, created_at, text):
        self.id = id
        self.created_at = created_at
        self.text = text.encode('utf-8')

    def __str__(self):
        return("Tweet:\n"
               "  id = {0}\n"
               "  created_at = {1}\n"
               "  text = {2}\n"
               .format(self.id, self.created_at, self.text))

def getTweets(filename):
	wb = open_workbook(filename)
	for sheet in wb.sheets():
	    number_of_rows = sheet.nrows
	    number_of_columns = sheet.ncols

	    items = []

	    rows = []
	    for row in range(1, number_of_rows):
	        values = []
	        for col in range(number_of_columns):
	            value  = (sheet.cell(row,col).value)
	            try:
	                value = str(int(value))
	            except ValueError:
	                pass
	            finally:
	                values.append(value)
	        item = Arm(*values)
	        items.append(item)
	return items

def getSentenceTags(items):
	Sentences = []
	partsOfSpeech = {}
	pairs = {} #NN NN
	pairs2 = {} #NN NNs
	pairs3 = {} #IN NN
	for item in items:
		temp = item.text.decode('ascii', errors="ignore")
		#temp = re.sub(r'\W+', ' ', temp)
		temp2 = ""
		sentenceStructure = []
		previous = ""
		previousPOS = ""
		for word in temp.split():
			if "http" not in word:
				word = re.sub(r'[^a-zA-Z0-9 - @ # . !]', '', word)
				word = re.sub(r'\s[0-9]+', '', word)
				word = word.lower()
			else:
			    word = re.sub(r'"', '', word)
			punctuation = ""
			if "http" in word:
				sentenceStructure.append("url")
				if "url" in partsOfSpeech:
					partsOfSpeech["url"].append(word)
				else:
					partsOfSpeech["url"] = []
					partsOfSpeech["url"].append(word)
				previous = word
				previousPOS = "url"
			else:
				temp = word
				if "." in word:
					punctuation = "."
					temp = word[:len(word)-1]
				elif "!" in word:
					punctuation = "!"
					temp = word[:len(word)-1]

				word = temp
				if "@" in word:
					sentenceStructure.append("ref")
					if "ref" in partsOfSpeech:
						partsOfSpeech["ref"].append(word)
					else:
						partsOfSpeech["ref"] = []
						partsOfSpeech["ref"].append(word)
					previous = word
					previousPOS = "ref"
				elif "#" in word:
					sentenceStructure.append("hashtag")
					if "hashtag" in partsOfSpeech:
						partsOfSpeech["hashtag"].append(word)
					else:
						partsOfSpeech["hashtag"] = []
						partsOfSpeech["hashtag"].append(word)
					previous = word
					previousPOS = "hashtag"
				elif "amp" == word:
					word = "&"
					sentenceStructure.append("amp")
					if "amp" in partsOfSpeech:
						partsOfSpeech["amp"].append(word)
					else:
						partsOfSpeech["amp"] = []
						partsOfSpeech["amp"].append(word)
					previous = word
					previousPOS = "amp"
				else:
					blob = TextBlob(word)
					for word2, pos in blob.tags:
						if previousPOS == "NN" and pos == "NN":
							if previous in pairs:
				        			pairs[previous].append(word2)
					        	else:
					        		pairs[previous] = []
					        		pairs[previous].append(word2)
					    	elif previousPOS == "NN" and pos == "NNS":
							if previous in pairs2:
				        			pairs2[previous].append(word2)
					        	else:
					        		pairs2[previous] = []
					        		pairs2[previous].append(word2)
					        elif previousPOS == "IN" and pos == "NN":
							if previous in pairs3:
				        			pairs3[previous].append(word2)
					        	else:
					        		pairs3[previous] = []
					        		pairs3[previous].append(word2)

						sentenceStructure.append(str(pos))
				        if str(pos) in partsOfSpeech:
				        	partsOfSpeech[str(pos)].append(word2)
				        else:
				        	partsOfSpeech[str(pos)] = []
				        	partsOfSpeech[str(pos)].append(word2)
				        previous = word2
					previousPOS = str(pos)
			if punctuation != "":
				sentenceStructure.append("punctuation")
				if "punctuation" in partsOfSpeech:
					partsOfSpeech["punctuation"].append(punctuation)
				else:
					partsOfSpeech["punctuation"] = []
					partsOfSpeech["punctuation"].append(punctuation)
		previous = ""
		previousPOS = ""
		Sentences.append(sentenceStructure)
	# print(pairs2)
	return Sentences, partsOfSpeech, pairs, pairs2, pairs3

test = getTweets('realDonaldTrump_tweets.xls')
actualTweets = {}
k = 0
for item in test:
	temp = item.text
	actualTweets[k] = temp
	k = k+1

derp = getSentenceTags(test)

sentenceCounter = Counter(str(e) for e in derp[0])
# print(derp[0])
# wordCounter = Counter(str(e) for e in derp[1]['NNS'])
#print counter.most_common(5)
#print wordCounter
tweetDict = {}
for i in range(0,10):
	testTweet = random.choice(derp[0])
	print(testTweet)
	tweet = ""
	previous = ""
	previousPOS = ""
	for part in testTweet:
		test = []
		if part == "NN" and previousPOS == "NN" and previous != "":
			wordCounter = Counter(str(e) for e in derp[2][previous])
			wordCounter = wordCounter.most_common(10)
			test = random.choice(wordCounter)
			tweet = tweet + " " + test[0]
			tweetDict[i] = tweet
			print("NN")
			print(previous)
			print(test[0])
		elif part == "NNS" and previousPOS == "NN" and previous != "":
			wordCounter = Counter(str(e) for e in derp[3][previous])
			wordCounter = wordCounter.most_common(10)
			test = random.choice(wordCounter)
			tweet = tweet + " " + test[0]
			tweetDict[i] = tweet
			print("NNS")
			print(previous)
			print(test[0])
		elif part == "NN" and previousPOS == "IN" and previous != "":
			wordCounter = Counter(str(e) for e in derp[4][previous])
			wordCounter = wordCounter.most_common(10)
			test = random.choice(wordCounter)
			tweet = tweet + " " + test[0]
			tweetDict[i] = tweet
			print("IN")
			print(previous)
			print(test[0])
		else:
			wordCounter = Counter(str(e) for e in derp[1][part])
			#print wordCounter
			wordCounter = wordCounter.most_common(10)
			test = random.choice(wordCounter)
			tweet = tweet + " " + test[0]
			tweetDict[i] = tweet

		previous = test[0]
		previousPOS = part
	tweetDict[i] = tweet

with open('data.txt', 'w') as outfile:
    json.dump(tweetDict, outfile)

with open('actualTweets.txt', 'w') as outfile:
    json.dump(actualTweets, outfile)
