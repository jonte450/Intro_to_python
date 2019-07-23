import math as m
from math import e

import random as r
from random import sample

# print e to the power of 3 using the math module
print(m.pow(e,3))


word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    return ''.join(r.sample(word_list,3))
    
    
# test your function
print(generate_password())
