# -*- coding: utf-8 -*-

import unicodedata
from stop_words import get_stop_words
import re

stopwords=get_stop_words('spanish')

def count(ustra):
	ustra=unicodedata.normalize('NFKD', ustra).encode('ASCII', 'ignore')
	ustra=ustra.lower()

	la_words=removeSymbolsAndWhiteSpaces(ustra)
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

def removeSymbolsAndWhiteSpaces(ustra):
	list=re.split('\W+',ustra)
	return list