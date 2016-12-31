doc1 = "Dumb, but happy... That's what I would want to be. It is not as easy, because being simple is not easy when you are intelligent, but it's worth a try"
import nltk
tokens = nltk.word_tokenize(doc1)
only_nouns_verbs_and_adjectives = []
tagged = nltk.pos_tag(tokens)
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

		

print(only_nouns_verbs_and_adjectives)

