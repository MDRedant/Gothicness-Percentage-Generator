k = open("bookinfolist.txt", "rt", encoding = "utf-8")
allthebooks = k.read()
k.close()
cleanedbooks = []
allbooks = allthebooks.split("\n")
allcleanedbooks = allbooks.remove(allbooks[0])
for book in allbooks:
	bookinfo = book.split("',")
	cleanedbookinfo = []
	for info in bookinfo:
		info = str(info)
		dob = info.replace( r"\ufeff", "")
		dab = dob.replace( r"'", "")
		dib = dab.replace( r"[", "")
		deb = dib.replace( r"]", "")
		cleanedbookinfo.append(deb)
	cleanedbooks.append(cleanedbookinfo)
mostgothicbooks = []
for book in cleanedbooks:
	bookpercentage = book[-1]
	nospace = bookpercentage.replace(" ", "")
	percentagefloat = float(nospace)
	if percentagefloat > 2:
		mostgothicbooks.append(book)
print(mostgothicbooks)
mostgothicbooktexts = []
import string
punctuation = set(string.punctuation)
cleantitles = [] 
for book in mostgothicbooks:
	booktitlepartz = []
	booktitle = book[0]
	booktitleparts = booktitle.split()
	firstword = booktitleparts[0].capitalize()
	secondword = list(booktitleparts)[1].capitalize()
	booktitlepartz.append(firstword)
	booktitlepartz.append(secondword)
	booktitleparty = []
	for part in booktitlepartz:
		booktitlesection = "".join(tse for tse in part if tse not in punctuation)
		booktitleparty.append(booktitlesection)
	cleanbooktitle = "_".join(booktitleparty)
	cleantitles.append(cleanbooktitle)
for book in cleantitles:
	bookdirectory = "C:\\Users\\Mickey\\Documents\\Github\\Gothicness-Percentage-Generator\\Gothic_novel_project\\gothic_novels" + "\\" + book + ".txt"
	t = open(bookdirectory, "rt", encoding = 'utf-8')
	noveltext = t.read()
	t.close()
	from nltk.corpus import stopwords
	stop = set(stopwords.words('english'))
	exclude = set(string.punctuation + string.digits)
	name = ['matilda', 'verezzi', 'zastrozzi', 'guiseppe', 'jerome', 'hippolita', 'manfred', 'frederic', 'bianca', 'isabella', 'theodore', 'glenarvon', 'avondale', 'calantha', 'emmeline', 'godolphin', 'lewis', 'clarke', 'merritt', 'philip', 'ellena', 'schedoni', 'vivaldi', 'adeline']
	def clean(doc):
		import nltk
		doc = str(doc)
		doc = doc.lower()
		stop_free = " ".join([i for i in doc.split() if i not in stop])
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
	textnovel = clean(noveltext)
	mostgothicbooktexts.append(textnovel)
import gensim	
from gensim import corpora, models
import numpy
dictionary = corpora.Dictionary(mostgothicbooktexts)
goth_work_matrix = [dictionary.doc2bow(gothicwork) for gothicwork in mostgothicbooktexts]
Lda = gensim.models.ldamodel.LdaModel(goth_work_matrix, num_topics = 10, id2word = dictionary, chunksize = 500, passes = 5, minimum_probability = 0 )
def get_gothicnessnumber(doc):
	topicdistribution = []
	numberoftexts = 0
	for text in goth_work_matrix:
		numberoftexts += 1
		topicdistribution.append(Lda[text])
	corpusaverages = []
	theme0 = 0
	theme1 = 0
	theme2 = 0
	theme3 = 0
	theme4 = 0
	theme5 = 0
	theme6 = 0
	theme7 = 0
	theme8 = 0
	theme9 = 0
	for book in topicdistribution:
		for theme in book:
			if theme[0] == 0:
				theme0 += theme[1]
			if theme[0] == 1:
				theme1 += theme[1]
			if theme[0] == 2:
				theme2 += theme[1]
			if theme[0] == 3:
				theme3 += theme[1]
			if theme[0] == 4:
				theme4 += theme[1]
			if theme[0] == 5:
				theme5 += theme[1]
			if theme[0] == 6:
				theme6 += theme[1]
			if theme[0] == 7:
				theme7 += theme[1]
			if theme[0] == 8:
				theme8 += theme[1]
			if theme[0] == 9:
				theme9 += theme[1]
	theme_0 = [0]
	theme0 = theme0/ numberoftexts
	theme_0.append(theme0)
	theme_1 = [1]
	theme1 = theme1/ numberoftexts
	theme_1.append(theme1)
	theme_2 = [2]
	theme2 = theme2/ numberoftexts
	theme_2.append(theme2)
	theme_3 = [3]
	theme3 = theme3/ numberoftexts
	theme_3.append(theme3)
	theme_4 = [4]
	theme4 = theme4/ numberoftexts
	theme_4.append(theme4)
	theme_5 = [5]
	theme5 = theme5/ numberoftexts
	theme_5.append(theme5)
	theme_6 = [6]
	theme6 = theme6/ numberoftexts
	theme_6.append(theme6)
	theme_7 = [7]
	theme7 = theme7/ numberoftexts
	theme_7.append(theme7)
	theme_8 = [8]
	theme8 = theme8/ numberoftexts
	theme_8.append(theme8)
	theme_9 = [9]
	theme9 = theme9/ numberoftexts
	theme_9.append(theme9)
	corpusaverages.append(theme_0)
	corpusaverages.append(theme_1)
	corpusaverages.append(theme_2)
	corpusaverages.append(theme_3)
	corpusaverages.append(theme_4)
	corpusaverages.append(theme_5)
	corpusaverages.append(theme_6)
	corpusaverages.append(theme_7)
	corpusaverages.append(theme_8)
	corpusaverages.append(theme_9)
	cleandoc = clean(doc)
	matr = dictionary.doc2bow(cleandoc)
	ldastuff = Lda[matr]
	together = list(zip(ldastuff, corpusaverages))
	togetheratlast = []
	sub0 = [0]
	sub1 = [1]
	sub2 = [2]
	sub3 = [3]
	sub4 = [4]
	sub5 = [5]
	sub6 = [6]
	sub7 = [7]
	sub8 = [8]
	sub9 = [9]
	for subs in together:
		for sub in subs:
			sub = list(sub)
			if sub[0] == 0:
				sub0.append(sub[1])
			if sub[0] == 1:
				sub1.append(sub[1])
			if sub[0] == 2:
				sub2.append(sub[1])
			if sub[0] == 3:
				sub3.append(sub[1])
			if sub[0] == 4:
				sub4.append(sub[1])
			if sub[0] == 5:
				sub5.append(sub[1])
			if sub[0] == 6:
				sub6.append(sub[1])
			if sub[0] == 7:
				sub7.append(sub[1])
			if sub[0] == 8:
				sub8.append(sub[1])
			if sub[0] == 9:
				sub9.append(sub[1])
			else:
				continue
	sub_0 = [sub0[0], (sub0[1]/sub0[2])]
	togetheratlast.append(sub_0)
	sub_1 = [sub1[0], (sub1[1]/sub1[2])]
	togetheratlast.append(sub_1)
	sub_2 = [sub2[0], (sub2[1]/sub2[2])]
	togetheratlast.append(sub_2)
	sub_3 = [sub3[0], (sub3[1]/sub3[2])]
	togetheratlast.append(sub_3)
	sub_4 = [sub4[0], (sub4[1]/sub4[2])]
	togetheratlast.append(sub_4)
	sub_5 = [sub5[0], (sub5[1]/sub5[2])]
	togetheratlast.append(sub_5)
	sub_6 = [sub6[0], (sub6[1]/sub6[2])]
	togetheratlast.append(sub_6)
	sub_7 = [sub7[0], (sub7[1]/sub7[2])]
	togetheratlast.append(sub_7)
	sub_8 = [sub8[0], (sub8[1]/sub8[2])]
	togetheratlast.append(sub_8)
	sub_9 = [sub9[0], (sub9[1]/sub9[2])]
	togetheratlast.append(sub_9)
	return togetheratlast
k = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness-Percentage-Generator\\Gothic_novel_project\\gothic_novels\\Carmilla.txt", "rt", encoding = 'utf-8')
testtext = k.read()
k.close()
testtext = clean(testtext)
print(get_gothicnessnumber(testtext))





		





