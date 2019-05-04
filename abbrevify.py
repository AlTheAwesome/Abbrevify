import string
import re

letters = list(string.ascii_lowercase)

def nothere(word):
	for i in word:
		if i in letters:
			letters.remove(i)
	return letters

#set1
# print(nothere("completely automated public turing test computers humans appart"))
# print(nothere("completely automated public turing test computers humans appart wired equivilant privacy"))
# print(nothere("completely automated public turing test computers humans appart wired equivilant privacy organization unique identifier"))
# print(nothere("completely automated public turing test computers humans appart wired equivilant privacy organization unique identifier joint photographic experts group"))
# print(nothere("completely automated public turing test computers humans appart wired equivilant privacy organization unique identifier joint photographic experts group disk operating system"))

#set2
print(nothere("national television system comitee")) #NTSC
print(nothere("national television system comitee standard commands programmable instrumentation hypertext markup language")) #HTML
print(nothere("national television system comitee standard commands programmable instrumentation hypertext markup language resource acquisition is initialization")) #RAII
print(nothere("national television system comitee standard commands programmable instrumentation hypertext markup language resource acquisition is initialization software project management")) #SPM
# print(nothere("national television system comitee standard commands programmable instrumentation")) #SCPI

#set3
# print(nothere("electronically erasable programmable read only memory")) #EEPROM
# print(nothere("electronically erasable programmable read only memory common object request broker architecture")) #CORBA
# print(nothere("electronically erasable programmable read only memory common object request broker architecture berkely open infastructure for network computing")) #BOINC
# print(nothere("electronically erasable programmable read only memory common object request broker architecture berkely open infastructure for network computing orthogonal frequency division multiplexing")) #OFDM
# print(nothere("electronically erasable programmable read only memory common object request broker architecture berkely open infastructure for network computing orthogonal frequency division multiplexing international standardization organization")) #ISO

# def places(word):
# 	placez = []
# 	for i in word:
# 		placez.append(letters.index(i))
# 	return placez
# print(places("iso"))