import string
import re
from database import * #I hate this too but I'm not re-writing this code...
import datetime
alter = int(str(datetime.date.today())[-2:]) # He He

Final = ""

encoded = input("What do you want to Decode?  ") #'22H213I702S623B702R311W111O40XX043E533E203O3'#"41C611C923I902S412S011W111W10XS023C103B502H0"  #input("What do you want Decoded?")
split = re.findall("\d[\d|\w]\w[\d|\w]", encoded)

length = len(split)
if length % 2 == 0:
	origin = length // 2 - 1
else:
	origin = length // 2
# origin = length / 2 - 1 if length % 2 == 0 else length // 2

split.insert(origin+1, split.pop())
split.insert(origin+1, split.pop(0))


abc = string.ascii_uppercase

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
	mod +=1


print(Final)

#even I don't really know what's going on...which is why this is such a great cryptography algorithm XDDD



# for ac in split:
# 	pt1 = int(ac[0] + ac[-1])
# 	pt2 = ac[1:3]
# 	print(pt1, pt2)
# 	set = globals()["SET" + pt2[0]]
# 	for dic in range(len(set) - 1):
# 		if pt2[0] == "X":
# 			print("TRUE")
# 		elif pt2[1] == abc[set[dic]['N'][0]]:
# 			print("hell yeah")


