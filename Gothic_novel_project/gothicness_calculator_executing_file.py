import gensim	
from gensim import corpora, models, similarities
import numpy
from nltk.corpus import stopwords
import string
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
random_seed = 17
state = numpy.random.seed(random_seed)
dic = corpora.Dictionary.load("dictionary")
gothic = corpora.BleiCorpus('gothicnesscorpus')
Lda = gensim.models.ldamodel.LdaModel(gothic, num_topics = 10, id2word = dic, random_state = state, chunksize = 100, passes= 40)
index = similarities.MatrixSimilarity.load('gothic_similarities')
def get_difference(doc):
	newfile = clean(doc)
	vec_bow = dic.doc2bow(newfile)
	vec_lda = Lda[vec_bow]
	sims = index[vec_lda]
	sims = sorted(enumerate(sims), key=lambda item: -item[1])
	return sims
def appoint_gothicness(doc):
	differences = get_difference(doc)
	print(differences)
	security = 0
	testdifferences1 = get_difference(testtext1)
	testdifferences2 = get_difference(testtext2)
	testdifferences3 = get_difference(testtext3)
	testdifferences4 = get_difference(testtext4)
	testdifferences5 = get_difference(testtext5)
	print(testdifferences1)
	print(testdifferences2)
	print(testdifferences3)
	print(testdifferences4)
	print(testdifferences5)
	if testdifferences1[0][0] == 1:
			security += 1
	if testdifferences2[0][0] != 1:
			security += 1
	if testdifferences3[0][0] == 1:
			security += 1
	if testdifferences4[0][0] == 1:
			security += 1
	if testdifferences5[0][0] != 1:
			security += 1
	if security == 5:
		if differences[0][0] == 1:
			print('This work is gothic.')
		else:
			print('This work is not gothic.')
	else:
		print('Try again.')
k = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\testfiles\\The_Hound_Of_The_Baskervilles.txt", "rt", encoding ="utf-8")
testtext1 = k.read()
k.close()
z = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\testfiles\\The_Story_Of_Porcelain.txt", "rt", encoding = 'utf-8')
testtext2 = z.read()
z.close()
t = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\testfiles\\The_Mysteries_Of_Udolpho.txt", "rt", encoding = 'utf-8')
testtext3 = t.read()
t.close()
o = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\testfiles\\The_Abbess.txt", "rt", encoding = 'utf-8')
testtext4 = o.read()
o.close()
a = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\testfiles\\Ulysses.txt", "rt", encoding = 'utf-8')
testtext5 = a.read()
a.close()
c = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\testfiles\\Pride_And_Prejudice.txt", "rt", encoding = 'utf-8')
text = c.read()
c.close()
print(appoint_gothicness(text))