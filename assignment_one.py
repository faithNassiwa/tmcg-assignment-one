'''
A python function that takes a list of SMS messages and input and returns 
a ranking of each words frequency
'''

def wordFreqDict(message_list): 
	message_string = ', '.join(message_list)  # converting list of messages to a string
	word_list = message_string.split()  # splits message_string into a list of words
	word_freq = [word_list.count(word) for word in word_list]  # count the frequency of each word's appearance in the word_list

	return dict(zip(word_list, word_freq))