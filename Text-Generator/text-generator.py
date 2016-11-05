import random, string
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxyz'
letters = string.ascii_lowercase

num_letters = int(raw_input("How many letters in this randomly generated name? "))
num_names = int(raw_input("How many names would you like to generate? "))

letter_input = []
for i in range(num_letters):
	letter_type = raw_input("#"+str(i+1)+": What letter do you want? Enter 'v' for vowels, 'c' for consonants, 'l' for any letter: ")
	letter_input.append(letter_type[0])


def generator(letter_input):
	name = ''
	for letter in letter_input:
		if letter == 'v':
			name = name+random.choice(vowels)
		elif letter=='c':
			name = name+random.choice(consonants)
		elif letter == 'l':
			name = name+random.choice(letters)
		else:
			name = name+letter
	return name

for i in range(num_names):
	print(generator(letter_input))
