import gensim	
from gensim import corpora, models, similarities
import numpy
import string
random_seed = 13
state = numpy.random.seed(random_seed)
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
		if word[1] == 'VP':
			only_nouns_verbs_and_adjectives.append(word[0])
		else:
			continue
	name_free = [tz for tz in only_nouns_verbs_and_adjectives if tz not in name]
	other_free = [tz for tz in name_free if tz not in other]
	return name_free
def get_similarities_with_eighteenth_century(doc):
	eighteenthcenturydict= corpora.Dictionary.load("eighteenthcenturydict")
	eighteenth = corpora.BleiCorpus('eighteenthcorpus')
	Lda = gensim.models.ldamodel.LdaModel(eighteenth, num_topics = 10, id2word = eighteenthcenturydict, random_state = state, chunksize = 100, passes= 40)
	index = similarities.MatrixSimilarity.load('similarities_with_eighteenth')
	newfile = clean(doc)
	vec_bow = eighteenthcenturydict.doc2bow(newfile)
	vec_lda = Lda[vec_bow]
	sims = index[vec_lda]
	sims = sorted(enumerate(sims), key=lambda item: -item[1])
	return sims
def get_similarities_with_early_nineteenth_century(doc):
	earlynineteenthcenturydict= corpora.Dictionary.load("earlynineteenthcenturydict")
	earlynineteenth = corpora.BleiCorpus('earlynineteenthcorpus')
	Lda = gensim.models.ldamodel.LdaModel(earlynineteenth, num_topics = 10, id2word = earlynineteenthcenturydict, random_state = state, chunksize = 100, passes= 40)
	index = similarities.MatrixSimilarity.load('similarities_with_early_nineteenth')
	newfile = clean(doc)
	vec_bow = earlynineteenthcenturydict.doc2bow(newfile)
	vec_lda = Lda[vec_bow]
	sims = index[vec_lda]
	sims = sorted(enumerate(sims), key=lambda item: -item[1])
	return sims
def get_similarities_with_late_nineteenth_century(doc):
	latenineteenthcenturydict= corpora.Dictionary.load("latenineteenthcenturydict")
	latenineteenth = corpora.BleiCorpus('earlynineteenthcorpus')
	Lda = gensim.models.ldamodel.LdaModel(latenineteenth, num_topics = 10, id2word = latenineteenthcenturydict, random_state = state, chunksize = 100, passes= 40)
	index = similarities.MatrixSimilarity.load('similarities_with_eighteenth')
	newfile = clean(doc)
	vec_bow = latenineteenthcenturydict.doc2bow(newfile)
	vec_lda = Lda[vec_bow]
	sims = index[vec_lda]
	sims = sorted(enumerate(sims), key=lambda item: -item[1])
	return sims
def get_similarities_with_twentieth_century(doc):
	twentiethcenturydict= corpora.Dictionary.load("earlytwentiethcenturydict")
	twentieth = corpora.BleiCorpus('earlytwentiethcorpus')
	Lda = gensim.models.ldamodel.LdaModel(twentieth, num_topics = 10, id2word = twentiethcenturydict, random_state = state, chunksize = 100, passes= 40)
	index = similarities.MatrixSimilarity.load('similarities_with_twentieth')
	newfile = clean(doc)
	vec_bow = twentiethcenturydict.doc2bow(newfile)
	vec_lda = Lda[vec_bow]
	sims = index[vec_lda]
	sims = sorted(enumerate(sims), key=lambda item: -item[1])
	return sims
def predict_timeperiod(doc):
	eighteen = get_similarities_with_eighteenth_century(doc)
	nineteen1 = get_similarities_with_early_nineteenth_century(doc)
	nineteen2 = get_similarities_with_late_nineteenth_century(doc)
	twenty = get_similarities_with_twentieth_century(doc)
	print(eighteen)
	print(nineteen1)
	print(nineteen2)
	print(twenty)
	eighteensim = 0
	number_of_texts1 = 0
	for i in eighteen:
		number_of_texts1 += 1
		eighteensim += i[1]
	earlynineteensim = 0
	number_of_texts2 = 0
	for d in nineteen1:
		number_of_texts2 += 1
		earlynineteensim += d[1]
	latenineteensim = 0
	number_of_texts3 = 0
	for f in nineteen2:
		number_of_texts3 += 1
		latenineteensim += f[1]
	twentysim = 0
	number_of_texts4 = 0
	for k in twenty:
		number_of_texts4 += 1
		twentysim += k[1]
	sim18 = eighteensim / number_of_texts1
	earlysim19 = earlynineteensim / number_of_texts2
	latesim19 = latenineteensim / number_of_texts3
	sim20 = twentysim / number_of_texts4
	numbers = []
	numbers.append(sim18)
	numbers.append(earlysim19)
	numbers.append(latesim19)
	numbers.append(sim20)
	if max(numbers) == sim18:
		print('The themes of this work show most similarity with themes of the 1751 to 1800 period.')
	if max(numbers) == earlysim19:
		print('The themes of this work show most similarity with themes of the 1801 to 1850 period.')
	if max(numbers) == latesim19:
		print('The themes of this work show most similarity with themes of the 1851 to 1900 period.')
	if max(numbers) == sim20:
		print('The themes of this work show most similarity with themes of the 1901 to 1950 period.')	
c = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\testfiles\\Ulysses.txt", "rt", encoding = 'utf-8')
text = c.read()
c.close()
print(predict_timeperiod(text))
c = open("C:\\Users\\Mickey\\Documents\\Github\\Gothicness_Generator\\Gothic_novel_project\\testfiles\\The_Great_God_Pan.txt", "rt", encoding = 'utf-8')
text = c.read()
c.close()
print(predict_timeperiod(text))
