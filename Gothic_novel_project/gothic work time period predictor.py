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
late_eighteenth_century = []
early_nineteenth_century = []
late_nineteenth_century = []
early_twentieth_century = []
for book in cleanedbooks:
	year = book[2].replace(" ", "")
	print(year)
	year = int(year)
	if year > 1900:
		early_twentieth_century.append(book)
	elif year > 1850:
		late_nineteenth_century.append(book)
	elif year > 1800:
		early_nineteenth_century.append(book)
	elif year <= 1800:
		late_eighteenth_century.append(book)
	else:
		continue
eightcenttitles = []
for book in late_eighteenth_century:
	booktitlepartz = []
	booktitle = book[0]
	booktitleparts = booktitle.split(punctuation)
	booktitlewords = booktitleparts[0]
	booktitlewordz = booktitlewords.split()
	for word in booktitlewordz:
		word = word.capitalize()
		booktitlepartz.append(word)
	booktitleparty = []
	for part in booktitlepartz:
		booktitlesection = "".join(tse for tse in part if tse not in punctuation)
		booktitleparty.append(booktitlesection)
	cleanbooktitle = "_".join(booktitleparty)
	eightcenttitles.append(cleanbooktitle)
eighteenthcenturybooks = []
for book in eightcenttitles:
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
	eighteenthcenturybooks.append(textnovel)
earlyninecenttitles = []
for book in late_eighteenth_century:
	booktitlepartz = []
	booktitle = book[0]
	booktitleparts = booktitle.split(punctuation)
	booktitlewords = booktitleparts[0]
	booktitlewordz = booktitlewords.split()
	for word in booktitlewordz:
		word = word.capitalize()
		booktitlepartz.append(word)
	booktitleparty = []
	for part in booktitlepartz:
		booktitlesection = "".join(tse for tse in part if tse not in punctuation)
		booktitleparty.append(booktitlesection)
	cleanbooktitle = "_".join(booktitleparty)
	earlyninecenttitles.append(cleanbooktitle)
earlynineteenthcenturybooks = []
for book in earlyninecenttitles:
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
	earlynineteenthcenturybooks.append(textnovel)
lateninecenttitles = []
for book in late_eighteenth_century:
	booktitlepartz = []
	booktitle = book[0]
	booktitleparts = booktitle.split(punctuation)
	booktitlewords = booktitleparts[0]
	booktitlewordz = booktitlewords.split()
	for word in booktitlewordz:
		word = word.capitalize()
		booktitlepartz.append(word)
	booktitleparty = []
	for part in booktitlepartz:
		booktitlesection = "".join(tse for tse in part if tse not in punctuation)
		booktitleparty.append(booktitlesection)
	cleanbooktitle = "_".join(booktitleparty)
	lateninecenttitles.append(cleanbooktitle)
latenineteenthcenturybooks = []
for book in lateninecenttitles:
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
	latenineteenthcenturybooks.append(textnovel)
earlytwentiethcenttitles = []
for book in late_eighteenth_century:
	booktitlepartz = []
	booktitle = book[0]
	booktitleparts = booktitle.split(punctuation)
	booktitlewords = booktitleparts[0]
	booktitlewordz = booktitlewords.split()
	for word in booktitlewordz:
		word = word.capitalize()
		booktitlepartz.append(word)
	booktitleparty = []
	for part in booktitlepartz:
		booktitlesection = "".join(tse for tse in part if tse not in punctuation)
		booktitleparty.append(booktitlesection)
	cleanbooktitle = "_".join(booktitleparty)
	earlytwentiethcenttitles.append(cleanbooktitle)
earlytwentiethcenturybooks = []
for book in earlytwentiethcenttitles:
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
	earlytwentiethcenturybooks.append(textnovel)


