import re

Long = input("insert Abbreviation with the first letters in Caps ")
Long = Long.replace(" ", "")

Short = "".join([i for i in Long if i==i.upper() and i!= " "]) #returns the first letters of the sentence

default = {'a': [],
           'b': [],
           'c': [],
           'd': [],
           'e': [],
           'f': [],
           'g': [],
           'h': [],
           'i': [],
           'j': [],
           'k': [],
           'l': [],
           'm': [],
           'n': [],
           'o': [],
           'p': [],
           'q': [],
           'r': [],
           's': [],
           't': [],
           'u': [],
           'v': [],
           'w': [],
           'x': [],
           'y': [],
           'z': []
            }

#now we've got all the information that we need let's make the dictionary

globals()[Short] = default.copy()


for i in range(len(Long)):
	if re.match("\w", Long[i]) and not(re.match("_", Long[i])):
		print(Long[i])
		globals()[Short][Long[i].lower()] += [i]

print(globals()[Short])

with open("database.py", "a") as db:
	x = "{"
	spaces = " " * (len(Short) + 4)
	for i in globals()[Short].items():
		if i[0] == "a":
			db.write(f"{Short} = {x}'{i[0]}': {i[1]},\n")
		elif i[0] == "z":
			db.write(f"{spaces}'{i[0]}': {i[1]}\n" + spaces + "}\n" + "\n")
		else:
			db.write(f"{spaces}'{i[0]}': {i[1]},\n")

#This is a nice little script for inserting dictionaries into another.py file. (Not much flexibility)





