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
import string
import re
punctuation = string.punctuation
eightcenttitles = []
for book in late_eighteenth_century:
	booktitlepartz = []
	booktitle = book[0]
	booktitleparts = re.split("[" + punctuation + "]+", booktitle)
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
	bookdirectory = "C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\gothic_novels" + "\\" + book + ".txt"
	t = open(bookdirectory, "rt", encoding = 'utf-8')
	noveltext = t.read()
	t.close()
	from nltk.corpus import stopwords
	stop = set(stopwords.words('english'))
	exclude = set(string.punctuation + string.digits)
	name = ['matilda', 'verezzi', 'zastrozzi', 'guiseppe', 'jerome', 'hippolita', 'manfred', 'frederic', 'bianca', 'isabella', 'antonia','clerval'
		'theodore', 'glenarvon', 'avondale', 'calantha', 'emmeline', 'godolphin', 'lewis', 'clarke', 'merritt', 'ambrosio', 'edwin', 'madeline', 'elizabeth'
		'philip', 'ellena', 'schedoni', 'vivaldi', 'adeline','morney','justine','bertrand','eugene','mary','oakendale','lorenzo','elisabeth','albert','vincent',
		'eugene','rollo','rodger','randal','laura', 'walter', 'laurette','rosaline','percival','enrico','vathek','catherine','philip','hepzibah','montoni',
		'phoebe','clifford','tilney','amine','pyncheon','nisida','carathis','wagner','chamont','giovanni', 'osbert', 'beatrice','owen','malcom','luc','roseline',
		'edmund','maddalena','duca','guiseppe','marcello','girolamo','ubaldo','bababalouk', 'nouronihar', 'monica','montreville','mowbray','valancourt','stafford',
		'maud','theodore','julia','jane','roger','redmond','seymour','gondimar','margaret', 'anne', 'mercurius','zofloya','scythrop','muchardus','leonardo','flosky',
		'marionetta','glowry','hilary','victoria','henriquez','berenza','lilla','carmilla','roderic','donald','allan','catharine','dungivan','hyde','jeckyll',
		'utterson','janette','ichabod','melmoth','elinor','isidora','john','annette','aubert', 'poole', 'megalena', 'marguerite', 'guiseppe', 'jannette', 'crisparkle',
		'jasper', 'twinkleton', 'neville', 'pleyel','lindon','lessingham','lucy','carwin','wieland','rosa','i', 'jonathan','oswald', 'paul','sydney', 'lovel', 'holt', 
		'joseph','leixlip','gulchenrouz','blaney', 'richard', 'clara','aubrey', 'morakanabad', 'fakredin']
	other = ['mr','i','man','woman','many', 'several','much','till', 'de','la','thy','thee','thou','caliph','motte','marquis','count', 'part','collogue', 'hand',
		'lord', 'lady','madame','sir','miss','mrs','st','marchese','chapter', '"i','duke','prince','princess','dont','thing','anything','something','nothing','heart',
		'day','night','moor','little','young','old','time','moment','toobad','dear','whole','grewgious', 'sandy','dr', 'baron', 'countess','marchioness','van', 'scene',
		'immalee','cypress','first','last','forth','life','full','eunuchs','giaour', 'let','hath', 'whilst','dutch','thane','name','person','head','indian','emir','jew',
		'donna', 'toll', 'great']
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
		other_free = [tz for tz in name_free if tz not in other]
		return name_free
	textnovel = clean(noveltext)
	eighteenthcenturybooks.append(textnovel)
earlyninecenttitles = []
for book in late_eighteenth_century:
	booktitlepartz = []
	booktitle = book[0]
	booktitleparts = re.split("[" + punctuation + "]+", booktitle)
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
	bookdirectory = "C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\gothic_novels" + "\\" + book + ".txt"
	t = open(bookdirectory, "rt", encoding = 'utf-8')
	noveltext = t.read()
	t.close()
	textnovel = clean(noveltext)
	earlynineteenthcenturybooks.append(textnovel)
lateninecenttitles = []
for book in late_eighteenth_century:
	booktitlepartz = []
	booktitle = book[0]
	booktitleparts = re.split("[" + punctuation + "]+", booktitle)
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
	bookdirectory = "C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\gothic_novels" + "\\" + book + ".txt"
	t = open(bookdirectory, "rt", encoding = 'utf-8')
	noveltext = t.read()
	t.close()
	textnovel = clean(noveltext)
	latenineteenthcenturybooks.append(textnovel)
earlytwentiethcenttitles = []
for book in late_eighteenth_century:
	booktitlepartz = []
	booktitle = book[0]
	booktitleparts = re.split("[" + punctuation + "]+", booktitle)
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
	bookdirectory = "C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\gothic_novels" + "\\" + book + ".txt"
	t = open(bookdirectory, "rt", encoding = 'utf-8')
	noveltext = t.read()
	t.close()
	textnovel = clean(noveltext)
	earlytwentiethcenturybooks.append(textnovel)
import gensim	
from gensim import corpora, models, similarities
import numpy
random_seed = 13
state = numpy.random.seed(random_seed)
dictionary18 = corpora.Dictionary(eighteenthcenturybooks)
dictionary18.save('eighteenthcenturydict')
eighteenthcenturydict= corpora.Dictionary.load("eighteenthcenturydict")
eighteenthcorpus = [eighteenthcenturydict.doc2bow(work) for work in eighteenthcenturybooks]
corpora.BleiCorpus.serialize('eighteenthcorpus', eighteenthcorpus)
eighteenth = corpora.BleiCorpus('eighteenthcorpus')
Lda = gensim.models.ldamodel.LdaModel(eighteenth, num_topics = 10, id2word = eighteenthcenturydict, random_state = state, chunksize = 100, passes= 40)
index18 = similarities.MatrixSimilarity(Lda[eighteenth])
index18.save('similarities_with_eighteenth')
dictionary19 = corpora.Dictionary(earlynineteenthcenturybooks)
dictionary19.save('earlynineteenthcenturydict')
earlynineteenthcenturydict= corpora.Dictionary.load("earlynineteenthcenturydict")
earlynineteenthcorpus = [earlynineteenthcenturydict.doc2bow(work) for work in earlynineteenthcenturybooks]
corpora.BleiCorpus.serialize('earlynineteenthcorpus', earlynineteenthcorpus)
earlynineteenth = corpora.BleiCorpus('earlynineteenthcorpus')
Lda = gensim.models.ldamodel.LdaModel(earlynineteenth, num_topics = 10, id2word = earlynineteenthcenturydict, random_state = state, chunksize = 100, passes= 40)
index19early = similarities.MatrixSimilarity(Lda[earlynineteenth])
index19early.save('similarities_with_early_nineteenth')
dictionary19late = corpora.Dictionary(latenineteenthcenturybooks)
dictionary19late.save('latenineteenthcenturydict')
latenineteenthcenturydict= corpora.Dictionary.load("latenineteenthcenturydict")
latenineteenthcorpus = [latenineteenthcenturydict.doc2bow(work) for work in latenineteenthcenturybooks]
corpora.BleiCorpus.serialize('latenineteenthcorpus', latenineteenthcorpus)
latenineteenth = corpora.BleiCorpus('latenineteenthcorpus')
Lda = gensim.models.ldamodel.LdaModel(latenineteenth, num_topics = 10, id2word = latenineteenthcenturydict, random_state = state, chunksize = 100, passes= 40)
index19late = similarities.MatrixSimilarity(Lda[latenineteenth])
index19late.save('similarities_with_late_nineteenth')
dictionary20 = corpora.Dictionary(earlytwentiethcenturybooks)
dictionary20.save('earlytwentiethcenturydict')
earlytwentiethcenturydict= corpora.Dictionary.load("earlytwentiethcenturydict")
earlytwentiethcorpus = [earlytwentiethcenturydict.doc2bow(work) for work in earlytwentiethcenturybooks]
corpora.BleiCorpus.serialize('earlytwentiethcorpus', earlytwentiethcorpus)
twentieth = corpora.BleiCorpus('earlytwentiethcorpus')
Lda = gensim.models.ldamodel.LdaModel(twentieth, num_topics = 10, id2word = earlytwentiethcenturydict, random_state = state, chunksize = 100, passes= 40)
index20 = similarities.MatrixSimilarity(Lda[twentieth])
index20.save('similarities_with_twentieth')