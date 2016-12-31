import os
novellist = []
cleannovellist = []
for novel in os.listdir("C:\\Users\\Mickey\\Documents\\Github\\Gothicness-Percentage-Generator\\Gothic_novel_project\\gothic_novels"):
	if novel.endswith(".txt"):
		noveldirectory = "C:\\Users\\Mickey\\Documents\\Github\\Gothicness-Percentage-Generator\\Gothic_novel_project\\gothic_novels" + "\\" + novel
		f = open(noveldirectory, "rt", encoding = "utf-8")
		textnovel = f.read()
		f.close()
		novellist.append(textnovel)
		from nltk.corpus import stopwords
		from nltk.stem.wordnet import WordNetLemmatizer
		import string
		stop = set(stopwords.words('english'))
		exclude = set(string.punctuation + string.digits)
		name = set(['matilda', 'verezzi', 'zastrozzi', 'guiseppe', 'jerome', 'hippolita', 'manfred', 'frederic', 'bianca', 'isabella', 'theodore', 'glenarvon', 'avondale', 'calantha', 'emmeline', 'godolphin', 'lewis', 'clarke', 'merritt', 'philip', 'ellena', 'schedoni'])
		lemma = WordNetLemmatizer()
		def clean(doc):
			import nltk
			stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
			punc_free = " ".join(ch for ch in stop_free if ch not in exclude)
			name_free = " ".join(ft for ft in punc_free if ft not in name)
			tokens = nltk.word_tokenize(name_free)
			tagged = nltk.pos_tag(tokens)
			only_nouns_verbs_and_adjectives = []
			for word in tagged:
				word = list(word)
				if word[1] == 'JJ':
					only_nouns_verbs_and_adjectives.append(word[0])
				if word[1] == 'NN':
					only_nouns_verbs_and_adjectives.append(word[0])
				if word[1] == 'FW':
					only_nouns_verbs_and_adjectives.append(word[0])
				if word[1] == 'VP':
					only_nouns_verbs_and_adjectives.append(word[0])
				else:
					continue
			return only_nouns_verbs_and_adjectives
		textnovel = clean(textnovel)
		cleannovellist.append(textnovel)
import gensim	
from gensim import corpora
dictionary = corpora.Dictionary(cleannovellist)
goth_work_matrix = [dictionary.doc2bow(gothicwork) for gothicwork in cleannovellist]
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(goth_work_matrix, num_topics=10, id2word = dictionary, passes = 20)
print(ldamodel.print_topics(num_topics=10, num_words=25))
#def get_percentage(doc):
	#corpus_percentage_vectors = []
	#for textnovel in cleannovellist:
			#corpus_percentage_vectors.append(Lda[textnovel])
	#corpus_average = numpy.average(numpy.array(corpus_percentage_vectors), axis = 0)
	#doc_average = numpy.average(numpy.array(Lda[doc]), axis = 0)
	#differences = numpy.linalg.norm(corpus_average - doc_average)
	#return differences
#t = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness-Percentage-Generator\\Gothic_novel_project\\gothic_novels\\Glenarvon.txt", "rt", encoding = "utf-8")
#testdoc = t.read()
#t.close()
#get_percentage(testdoc)



		
		






