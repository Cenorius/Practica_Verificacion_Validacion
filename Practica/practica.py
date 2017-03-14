# -*- coding: utf-8 -*-

import unicodedata
from stop_words import get_stop_words

stopwords=get_stop_words('spanish')

def count(ustra):
	ustra=unicodedata.normalize('NFKD', ustra).encode('ASCII', 'ignore')
	ustra=ustra.lower()

	la_words=ustra.split(" ")

	la_words=removeSymbols(la_words)
	la_words=removeStopwords(la_words)

	la_frecuencies=[]
	for w in la_words:
		la_frecuencies.append(la_words.count(w))

	lcount=zip(la_words, la_frecuencies)
	
	lcount=sorted(set(lcount),key=lambda x:x[1])
	
	return lcount

def removeStopwords(la_words):
	la_words=[w for w in la_words if w not in stopwords]
	return la_words

def removeSymbols(la_words):
	la_words=[e for e in la_words if e.isalnum()]
	return la_words