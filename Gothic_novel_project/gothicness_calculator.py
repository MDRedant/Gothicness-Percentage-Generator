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
mostgothicbooktexts = []
import string
punctuation = string.punctuation
cleantitles = [] 
import re 
for book in mostgothicbooks:
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
	cleantitles.append(cleanbooktitle)
corpuslength = 0
for book in cleantitles:
	bookdirectory = "C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\gothic_novels" + "\\" + book + ".txt"
	t = open(bookdirectory, "rt", encoding = 'utf-8')
	noveltext = t.read()
	t.close()
	corpuslength += len(noveltext)
	from nltk.corpus import stopwords
	stop = set(stopwords.words('english'))
	exclude = set(string.punctuation + string.digits)
	name = ['matilda', 'verezzi', 'zastrozzi', 'guiseppe', 'jerome', 'hippolita', 'manfred', 'frederic', 'bianca', 'isabella', 'antonia','clerval',
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
			if word[1] == 'VB':
				only_nouns_verbs_and_adjectives.append(word[0])
			else:
				continue
		name_free = [tz for tz in only_nouns_verbs_and_adjectives if tz not in name]
		other_free = [tk for tk in name_free if tk not in other]
		return other_free
	textnovel = clean(noveltext)
	mostgothicbooktexts.append(textnovel)
import gensim	
from gensim import corpora, models, similarities
import numpy
random_seed = 17
state = numpy.random.seed(random_seed)
dictionary = corpora.Dictionary(mostgothicbooktexts)
dictionary.save("dictionary")
dic= corpora.Dictionary.load("dictionary")
goth_work_matrix = [dic.doc2bow(gothicwork) for gothicwork in mostgothicbooktexts]
corpora.BleiCorpus.serialize('gothicnesscorpus', goth_work_matrix)
gothic = corpora.BleiCorpus('gothicnesscorpus')
Lda = gensim.models.ldamodel.LdaModel(gothic, num_topics = 10, id2word = dic, random_state = state, chunksize = 100, passes= 40)
index = similarities.MatrixSimilarity(Lda[gothic])
index.save('gothic_similarities')