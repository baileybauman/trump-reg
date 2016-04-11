from textblob import TextBlob
from xlrd import open_workbook
from collections import Counter
import random
from random import randrange
import re

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
	for item in items:
		temp = item.text.decode('ascii', errors="ignore")
		#temp = re.sub(r'\W+', ' ', temp)
		temp2 = ""
		sentenceStructure = []
		for word in temp.split():
			if "http" not in word:
				word = re.sub(r'[^a-zA-Z0-9 - @ #]', '', word)
				word = re.sub(r'\s[0-9]+', '', word)
			else:
			    word = re.sub(r'"', '', word)

			if "http" in word:
				sentenceStructure.append("url")
				if "url" in partsOfSpeech:
					partsOfSpeech["url"].append(word)
				else:
					partsOfSpeech["url"] = []
					partsOfSpeech["url"].append(word)
			elif "@" in word:
				sentenceStructure.append("ref")
				if "ref" in partsOfSpeech:
					partsOfSpeech["ref"].append(word)
				else:
					partsOfSpeech["ref"] = []
					partsOfSpeech["ref"].append(word)
			elif "#" in word:
				sentenceStructure.append("hashtag")
				if "hashtag" in partsOfSpeech:
					partsOfSpeech["hashtag"].append(word)
				else:
					partsOfSpeech["hashtag"] = []
					partsOfSpeech["hashtag"].append(word)
			else:
				blob = TextBlob(word)
				for word2, pos in blob.tags:
					sentenceStructure.append(str(pos))
			        if str(pos) in partsOfSpeech:
			        	partsOfSpeech[str(pos)].append(word2)
			        else:
			        	partsOfSpeech[str(pos)] = []
			        	partsOfSpeech[str(pos)].append(word2)
		Sentences.append(sentenceStructure)
	return Sentences, partsOfSpeech

test = getTweets('realDonaldTrump_tweets.xls')
derp = getSentenceTags(test)

sentenceCounter = Counter(str(e) for e in derp[0])
wordCounter = Counter(str(e) for e in derp[1]['NNS'])
#print counter.most_common(5)
#print wordCounter
testTweet = random.choice(derp[0])
tweet = ""
for part in testTweet:
	wordCounter = Counter(str(e) for e in derp[1][part])
	#print wordCounter
	wordCounter = wordCounter.most_common(10)
	test = random.choice(wordCounter)
	tweet = tweet + " " + test[0]

print tweet