import os
novellist = []
cleannovellist = []
for novel in os.listdir("C:\\Users\\Mickey\\Documents\\UAntwerpen\\programmeren\\Gothic_novel_project\\gothic_novels"):
	if novel.endswith(".txt"):
		noveldirectory = "C:\\Users\\Mickey\\Documents\\UAntwerpen\\programmeren\\Gothic_novel_project\\gothic_novels" + "\\" + novel
		f = open(noveldirectory, "rt", encoding = "utf-8")
		textnovel = f.read()
		f.close()
		novellist.append(textnovel)
		from nltk.corpus import stopwords
		from nltk.stem.wordnet import WordNetLemmatizer
		import string
		stop = set(stopwords.words('english'))
		exclude = set(string.punctuation)
		lemma = WordNetLemmatizer()
		def clean(doc):
			stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
			punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
			normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
			return normalized
		textnovel = clean(textnovel).split()
		cleannovellist.append(textnovel)
import gensim	
from gensim import corpora
dictionary = corpora.Dictionary(cleannovellist)
goth_work_matrix = [dictionary.doc2bow(gothicwork) for gothicwork in cleannovellist]
Lda = gensim.models.ldamodel.LdaModel
ldamodel = Lda(goth_work_matrix, num_topics=10)

print(ldamodel.print_topics(num_topics=10, num_words=30))



		
		






