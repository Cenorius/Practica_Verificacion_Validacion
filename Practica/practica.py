import unicodedata

stopwords=['la','me','el']

def count(ustra):
	ustra=unicodedata.normalize('NFKD', ustra).encode('ASCII', 'ignore')
	ustra=ustra.lower()

	la_words=ustra.split(" ")
	la_frecuencies=[]

	la_words=removeStopwords(la_words,stopwords)

	for w in la_words:
		la_frecuencies.append(la_words.count(w))

	lcount=zip(la_words, la_frecuencies)
	
	lcount=sorted(set(lcount),key=lambda x:x[1])
	
	return lcount

def removeStopwords(la_words, stopwords):
	for w in la_words:
		if w in stopwords:
			la_words.remove(w)
	return la_words