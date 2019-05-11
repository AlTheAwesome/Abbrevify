import string
import re
from database import * #I hate this too but I'm not re-writing this code...
import datetime
import os
import sys
alter = int(str(datetime.date.today())[-2:]) # He He

encoded = " ".join(sys.argv[1:]) #input("What do you want to Decode?  ") 

def Decrypt(encoded):

	Final = ""
	
	split = re.findall("\d[\d|\w]\w[\d|\w]", encoded)
	
	length = len(split)
	if length % 2 == 0:
		origin = length // 2 - 1
	else:
		origin = length // 2
	
	#I honestly don't know what's going on here....time for the notebook
	
	split.insert(origin+1, split.pop())
	split.insert(origin+1, split.pop(0)) 
	#takes the two edge letters and inserts them into the middle of the list
	
	abc = string.ascii_lowercase
	ABC = string.ascii_uppercase
	
	# print(split)
	
	mod = 0
	for i in range(len(split)):
		if i%2 == 0:
			origin = origin - mod
		else:
			origin = origin + mod
		# print(origin)
		ac = split[origin]
		pt1 = int(ac[0] + ac[-1])
		pt2 = ac[1:3]
		# print(pt1, pt2)
		set = globals()["SET" + pt2[0]]
		for dic in range(len(set) - 1):
			# print(pt2[1])
			if pt2[1] == abc[int(set[dic]['N'][0])]:
				for letta in set[dic].items():
					if pt1 in letta[1]:
						Final+= letta[0]
	
			elif pt2[1] == ABC[int(set[dic]['N'][0])]:
				for letta in set[dic].items():
					if pt1 in letta[1]:
						Final+= letta[0].upper()
		mod +=1
	
	
	print(Final)
	return(Final)
