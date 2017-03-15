# -*- coding: utf-8 -*-

import unicodedata
from stop_words import get_stop_words
import re

stopwords=get_stop_words('spanish')

def count(ustra):

	if(not isinstance(ustra, (str, unicode))):
		raise TypeError("The type must be str or unicode")

	if(isinstance(ustra, str)):
		ustra=unicode(ustra,'utf-8','ignore')

	ustra=unicodedata.normalize('NFKD', ustra).encode('ASCII', 'ignore')
	
	ustra=ustra.lower()
	
	la_words=removeSymbolsAndWhiteSpaces(ustra)
	la_words=removeStopwords(la_words)

	lcount=getWordsFrecuencies(la_words)
	
	lcount=sorted(lcount,key=lambda x:x[1])
	
	return lcount

def removeStopwords(la_words):
	la_words=[w for w in la_words if w not in stopwords]
	return la_words

def removeSymbolsAndWhiteSpaces(ustra):
	list=re.split('\W+',ustra)
	list=[w for w in list if (w is not '') and (w is not u'')]
	return list

def getWordsFrecuencies(la_words):
	if(not isinstance(la_words, list)):
		raise TypeError("The type must be list")
	print(la_words)
	la_frecuencies=[]

	for w in la_words:
		if(not isinstance(w, (str, unicode))):
			raise TypeError("The list elements must be str or unicode")
		la_frecuencies.append(la_words.count(w))
	
	lcount=zip(la_words, la_frecuencies)
	lcount=set(lcount)
	lcount=list(lcount)
	
	return lcount

if __name__ == "__main__":
	tstr='bicicleta,bicicletá hola @bièn bién bien ©"'
	tstr=count(tstr)