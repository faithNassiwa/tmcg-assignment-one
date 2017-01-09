'''
A python function that takes a list of SMS messages and returns 
a ranking of each word's frequency in a dictionary
'''
import re

def WordFreqDict(message_list): 
	message_string = ' , '.join(message_list)  # converting the list (message_list) to a string
	word_list = re.split("[, \-!?:]+", message_string)  # splitting message_string into a list of words minus provided punctuations
	word_freq = [word_list.count(word) for word in word_list]  # counting the frequency of each word's appearance in the word_list

	return dict(zip(word_list, word_freq))
