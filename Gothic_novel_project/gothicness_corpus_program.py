import os
novellist = []
cleannovellist = []
for novel in os.listdir("C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\gothic_novels"):
	if novel.endswith(".txt"):
		noveldirectory = "C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\gothic_novels" + "\\" + novel
		f = open(noveldirectory, "rt", encoding = "utf-8")
		textnovel = f.read()
		f.close()
		novellist.append(textnovel)
		from nltk.corpus import stopwords
		import string
		stop = set(stopwords.words('english'))
		exclude = set(string.punctuation + string.digits)
		name = ['matilda', 'verezzi', 'zastrozzi', 'guiseppe', 'jerome', 'hippolita', 'manfred', 'frederic', 'bianca', 'isabella', 'theodore', 'glenarvon', 
		'avondale', 'calantha', 'emmeline', 'godolphin', 'lewis', 'clarke', 'merritt', 'philip', 'ellena', 'schedoni', 'vivaldi', 'adeline']
		def clean(doc):
			import nltk
			stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
			punc_free = "".join(ch for ch in stop_free if ch not in exclude)
			tokens = nltk.word_tokenize(punc_free)
			tagged = nltk.pos_tag(tokens)
			only_nouns_verbs_and_adjectives = []
			for word in tagged:
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
			name_free = [tz for tz in only_nouns_verbs_and_adjectives if tz not in name]
			return name_free
		textnovel = clean(textnovel)
		cleannovellist.append(textnovel)
import gensim	
from gensim import corpora
dictionary = corpora.Dictionary(cleannovellist)
goth_work_matrix = [dictionary.doc2bow(gothicwork) for gothicwork in cleannovellist]
Lda = gensim.models.ldamodel.LdaModel
Ldamodel = Lda(goth_work_matrix, num_topics = 10, id2word = dictionary, passes = 7, minimum_probability = 0 )
distr_of_topics_per_book = []
for i in range(len(cleannovellist)):
	distr_of_topics_per_book.append(Ldamodel[goth_work_matrix[i]])
percentages = []
booknumber = 0
for book in distr_of_topics_per_book:
	gothicness = 0
	for theme in book:
		if theme[1] > 0.09:
			gothicness += 1
		else:
			continue
	booknumber += 1
	gothicnesspercentage = booknumber , gothicness
	percentages.append(gothicnesspercentage)
bookinformation = []
for novel in novellist:
	informationlist = []
	text = novel.split('\n')
	name = text[0]
	author = text[2]
	publication_date = text[4]
	informationlist.append(name)
	informationlist.append(author)
	informationlist.append(publication_date)
	bookinformation.append(informationlist)
bookdatalist = list(zip(bookinformation, percentages))
everything_equallist = []
for book in bookdatalist:
	togetherlist = []
	if book[0]:
		togetherlist.append(book[0][0])
		togetherlist.append(book[0][1])
		togetherlist.append(book[0][2])
	if book[-1]:
		togetherlist.append(book[1][1])
	everything_equallist.append(togetherlist)
dob = open('bookinfolist.txt', 'wt', encoding = 'utf-8')
for item in everything_equallist:
	dob.write("\n" + str(item))
dob.close()






		
		






