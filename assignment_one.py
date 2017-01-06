'''
A python function that takes a list of SMS messages and input and returns 
a ranking of each word's frequency
'''
import re

def wordFreqDict(message_list): 
	message_string = ' , '.join(message_list)  # converting list(message_list) to a string
	word_list = re.split("[, \-!?:]+", message_string)  # splits message_string into a list of words minus listed punctuations
	word_freq = [word_list.count(word) for word in word_list]  # count the frequency of each word's appearance in the word_list

	return dict(zip(word_list, word_freq))
