import random, re

### has form TOKEN_SEQUENCE : DICT OF { NEXT_TOKEN : COUNT }
###	     e.g        "a b c" : {"d" : 4, "e" : 2, "f" : 6 }
counts = {}

SEP = " "	# token separator symbol

def make_ngrams(tokens, n):
	""" Returns a list of n-long ngrams from a list of tokens """

	ngrams = []
	for i in range(len(tokens)-n+1):
		ngrams.append(tokens[i:i+n])
	return ngrams


def ngram_freqs(ngrams):
	""" Builds dict of TOKEN_SEQUENCEs and NEXT_TOKEN frequencies """

	# Using example of ngram "a b c e" ...
	for ngram in ngrams:
		token_seq  = SEP.join(ngram[:-1])	# "a b c"
		last_token = ngram[-1]				# "e"

		# create empty {NEXT_TOKEN : COUNT} dict if token_seq not seen before
		if token_seq not in counts:
			counts[token_seq] = {};

		# initialize count for newly seen next_tokens
		if last_token not in counts[token_seq]:
			counts[token_seq][last_token] = 0;

		counts[token_seq][last_token] += 1;


def next_word(text, n):
	""" Takes the text so far, and outputs the next word to add """

	token_seq = SEP.join(text.split()[-(n-1):]);
	choices = counts[token_seq].items();

	# make a weighted choice for the next_token
	# [see http://stackoverflow.com/a/3679747/2023516]
	total = sum(w for c, w in choices)
	r = random.uniform(0, total)
	upto = 0
	for c, w in choices:
		upto += w;
		if upto > r: return c
	assert False 							# should not reach here


def preprocess_corpus(filename):
	""" Basic pre-processing to prepare token list """

	s = open(filename, 'r').read()					# read in raw string
	s = re.sub('[-()]', r'', s)						# remove certain punctuation chars
	s = re.sub('([.,!?])', r' \1 ', s)				# pad certain punctuation chars with whitespace
	s = ' '.join(s.split()).lower()					# remove extra whitespace (incl. newlines)
	return s;

def postprocess_output(s):
	s = re.sub('\\s+([.,!?])\\s+', r'\1 ', s)		# correct whitespace padding around punctuation
	return s


if __name__ == "__main__":

	N = 3;
	text_len = 100;

	text = preprocess_corpus("corpus.txt")

	ngrams = make_ngrams(text.split(SEP), N)
	ngram_freqs(ngrams)

	#seed = "join us"
	seed = random.choice(counts.keys());
	rand_text = seed;

	for i in range(text_len):
		rand_text += SEP + next_word(rand_text, N);

	print postprocess_output(rand_text);