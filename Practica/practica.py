
def count(stra):

	la_words=stra.split(" ")
	la_frecuencies=[]

	for w in la_words:
		la_frecuencies.append(la_words.count(w))

	lcount=zip(la_words, la_frecuencies)
	
	lcount=sorted(set(lcount),key=lambda x:x[1])

	return lcount

