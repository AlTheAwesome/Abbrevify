import re
import string
import random
import database
import datetime
import sys
alter = int(str(datetime.date.today())[-2:]) #He He


raw = " ".join(sys.argv[1:])
#so now we have the string we want to encode

encoded = []

def name(word):
	result= []
	lettaz = string.ascii_lowercase
	for i in word:
		result.append(lettaz[int(i)])
	return "".join(result)

variance = x = 0
for i in range(len(raw)):
	x = 1 if i%2 == 0 else -1
	if raw[i] in string.ascii_lowercase:
		letter = raw[i]
		set = database.SETS[random.randint(0, (len(database.SETS) - 2))] #set Select
		abb = set[random.randint(0, (len(set) - 2))] #abbrev select

		while len(abb[raw[i]]) == 0:
			abb = set[random.randint(0, (len(set) - 2))]

		pos = abb[raw[i]][random.randint(0, len(abb[raw[i]]) - 1)] #pos of letR
		# print(name(abb['N'])[0].upper())

		if pos > 9:
			new = [str(pos)[0], set[-1] + name(abb['N'])[0].upper(), str(pos)[1]]
		else:
			new = ['0', set[-1] + name(abb['N'])[0].upper(), str(pos)[0]]

		encoded.insert(x, new)
		# print(encoded)
	else:
		SETX = database.SETX

		if raw[i] in string.digits:
			abb = SETX[random.randint(0, len(SETX) - 3)]
			while abb[raw[i]] == []:
				abb = SETX[random.randint(0, len(SETX) - 3)]
		else:
			abb = SETX[-2]

		pos = abb[raw[i]][random.randint(0, len(abb[raw[i]]) - 1)]

		if pos > 9:
			new = [str(pos)[0], SETX[-1] + name(abb['N'])[0].upper(), str(pos)[1]]
		else:
			new = ['0', SETX[-1] + name(abb['N'])[0].upper(), str(pos)[0]]

		encoded.insert(x, new)


for j in range(len(encoded)):
	encoded[j] = "".join(encoded[j])
print("".join(encoded))





	# print(f"letter: {letter},\n abb: {name(abb['N']).upper()},\n position: {pos}")
