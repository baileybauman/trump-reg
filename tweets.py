#!/usr/bin/python
# Bailey Bauman
# CSCE 470
# To be used for TrumpReg project

import re
import sys
import glob, os
import copy
import math
import operator
import random
import collections
import csv

# this will hold information about each word used in all of the files

class Entry:
    documents = {} 
    df = 0
    idf = 0

    def __init__(self):
        self.documents = {}
        self.df = 0
        self.idf = 0

    def addDocument(self, doc):
        if doc not in self.documents:
            self.documents[doc] = 1
        else:
            self.documents[doc] += 1

    def setTF(self):
        for doc in self.documents:
            self.documents[doc] = 1+math.log10(self.documents[doc])

    def setDF(self):
        self.df = len(self.documents)

    def setIDF(self, totalDocs):
        self.idf = math.log10(float(totalDocs) / self.df)

    def setTFIDF(self):
        for doc in self.documents:
            self.documents[doc] = self.documents[doc] * self.idf

    def getDocuments(self):
        return self.documents

    def containsDoc(self, doc):
        return doc in self.documents

    def getDocValue(self, doc):
        return self.documents[doc]

    def getDF(self):
        return self.df

    def __str__(self):
        return "[df: %s, idf:%s, doc/tfidf: %s]" %(self.df,self.idf, str(self.documents))

# print overall dictionary in a readable format
def printDictionary(dictionary):
    for word in dictionary:
        print "%s : %s" %(word,dictionary[word])
  
def getDocVector(filename):
    dictionary = {}
    counts = {}
    docID = 0
    filenames = []

    # new file
    with open(filename) as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            line = row["text"]
            line = line.lower()
            # line = re.sub(r'[^a-zA-Z0-9 - @ #]', ' ', line)
            # line = re.sub(r'\s[0-9]+', ' ', line)

            # new word
            for word in line.split():
                if "http" not in word:
                    word = re.sub(r'[^a-zA-Z0-9 - @ #]', '', word)
                    word = re.sub(r'\s[0-9]+', '', word)
                else:
                    word = re.sub(r'"', '', word)
                
                # word meets requirements to be added to dictionary
                if len(word) > 2:        
                    if word not in dictionary:
                        entry = Entry()
                        entry.addDocument(row["id"])
                        dictionary[word] = entry
                        counts[word] = 1

                    # already in dictionary, update occurrences
                    else:
                        dictionary[word].addDocument(row["id"])
                        counts[word] += 1
              
            docID = docID + 1      
        #printDictionary(dictionary)      
    #print docID
    words = {}
    #print counts
    for word in dictionary:
        words[word] = 0
        dictionary[word].setTF()
        dictionary[word].setDF()
        s = dictionary[word].getDF()
        words[word] = s
        dictionary[word].setIDF(docID)
        dictionary[word].setTFIDF()
    printDictionary(dictionary)  
    docVector = {}
    #make vector for each doc
    for doc in filenames:
        docVector[doc] = []
        for word in dictionary:
            if dictionary[word].containsDoc(doc):
                docVector[doc].append(dictionary[word].getDocValue(doc))
            else:
                docVector[doc].append(0)
    
    sorted_words = sorted(counts.iteritems(), key=operator.itemgetter(1), reverse=True)
    print "Total number of words: %d" % len(words)
    print "Total number of tweets: %d" % docID
    print "Most occuring words:"
    for i in range(0,min(50,docID)):
        print "%d. %s -" % (i+1,sorted_words[i][0]), sorted_words[i][1]

    return [docVector, filenames, len(dictionary), words]


filename = raw_input("Enter filename with Donald Trump's Tweets: ")

[docVector,filenames,totalWords,words] = getDocVector(filename)
