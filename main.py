import os
import re

from statistics import mean

def clean_input_text(t):

	with open(t) as f:

		lines = f.readlines()
		clean_lines = []
		for line in lines:
			clean_line = line.replace('...','.').replace('!', '.').replace('?', '.').replace('’', "'").replace('‘', "'").replace("–", ".").replace(":", ".").replace(";",".").replace("?!", ".").replace("!?",".").replace('‘', '').replace('„','').replace("“","").replace('-',' ').replace(',','').replace('"','').replace('“','').replace('”','').replace('(','').replace(')','').replace('[','').replace(']','')
			clean_lines.append(clean_line.strip())

		TEXT = ".".join(clean_lines)
		return(TEXT)

##################################################################

def word_count(text):

	re_pattern = "[a-zA-ZßäöüÄÖÜ]+\\'?[a-zA-ZßäöüÄÖÜ]*'?[a-zA-ZßäöüÄÖÜ]*" # letters and apostrophes.
	word_list = re.findall(re_pattern, text)
	WORD_COUNT = len(word_list)

	return WORD_COUNT

##################################################################

def sent_length(text):

	re_pattern = "[a-zA-ZßäöüÄÖÜ]+\\'?[a-zA-ZßäöüÄÖÜ]*\\'?[a-zA-ZßäöüÄÖÜ]*\\.?" # letters, apostrophes and full stops	
	word_list = re.findall(re_pattern, text)
	cleaned_text = " ".join(word_list)

	sent_list = cleaned_text.split('.')

	sent_lengths = []
	for sent in sent_list:
		if len(sent) > 1:

			sent = sent.lstrip()
			word_list = sent.split(" ")
			num_words = 0
			for word in word_list:
				if word != "":
					num_words += 1
			sent_lengths.append(num_words)

	try:
		SENT_LENm = round(mean(sent_lengths), 3)

	except:
		SENT_LENm = sent_lengths[0]
        
	return SENT_LENm

##################################################################

def word_length(text):

	re_pattern = "[a-zA-ZßäöüÄÖÜ]+\\'?[a-zA-ZßäöüÄÖÜ]*\\'?[a-zA-ZßäöüÄÖÜ]*" # letters and apostrophes
	word_list = re.findall(re_pattern, text)

	# count number of letters in each word and append to list
	word_lengths = []
	for word in word_list:

		num_chars = 0
		for char in word:
			if char != "'":
				num_chars += 1
		word_lengths.append(num_chars)

	WORD_LENm = round(mean(word_lengths), 3)

	return round(WORD_LENm, 3)
    
##################################################################
    
def get_data():
    
	fname = os.path.join('input_text.txt')
	TEXT = clean_input_text(fname)
	WORD_COUNT = word_count(TEXT)
	SENT_LENm = sent_length(TEXT)
	WORD_LENm = word_length(TEXT)

	return SENT_LENm, WORD_LENm

##################################################################

def get_cefr(sl, wl):

	sent_lens = [5.8,7.1,8.1,11.4,13.9,14.4]
	word_lens = [4.7,4.8,4.9,5.4,5.6,6.4]

	cefr_levels = ['A1','A2','B1','B2','C1','C2']

	cefr_index = [0,1,2,3,4,5]
	
	sent_number = min(sent_lens, key=lambda x:abs(x-sl)) # finds the sentence length in the list closest to the input
	word_number = min(word_lens, key=lambda x:abs(x-wl)) # finds the word length in the list closest to the input
	
	sent_index = sent_lens.index(sent_number)
	word_index = word_lens.index(word_number)

	# more weighting given to sentence lengths...
	weighted_index = (sent_index * .75) + (word_index * .25)

	# finds index number closest to weighted index (Python's round function is rubbish for rounding .5 floats correctly)

	overall_index = min(cefr_index, key=lambda x:abs(x-weighted_index))

	print('\nThe overall CEFR level of your text is approximately:', cefr_levels[overall_index])

	print('\nThe average length of sentences in your text is', sl, 'words. This corresponds to a level of about', cefr_levels[sent_index], 'on the Common European Framework of Reference.\n')

	print("\nThe average length of words in your text is", wl, "characters. \
	This corresponds to a level of about", cefr_levels[sent_index], "on the Common European Framework of Reference. \
	This may seem like a small number, considering that German is well-known for its very long compound words. \
	That's because this program counts all words, including smaller function words. The more grammatically complex a text is, the more of these smaller function words there is likely to be.\
	For this reason, word length is given less weight in calculating the overall complexity score.")

##################################################################

sl, wl = get_data()
get_cefr(sl, wl)
