'''
*********** Arun Shyam************
********** April 15, ..13***********

File for processing the input file.
I split the input file into three text files named :
circuits, jugglers and preferences respectively.

'''

import string
import re

# circuit, juggler and preferences list resp.
C_list=[]
J_list=[]
P_list=[]

#open necessary files
linestring = open("/home/arun/Desktop/juggler/text_process/input.txt", 'r').readlines()
cfile=open("/home/arun/Desktop/juggler/text_process/circuit.txt", 'w+')
jfile=open("/home/arun/Desktop/juggler/text_process/juggler.txt", 'w+')
pfile=open("/home/arun/Desktop/juggler/text_process/preferences.txt", 'w+')

#main processing logic
for i in range(len(linestring)):
	line=re.findall(r'\d+',linestring[i])
	if(linestring[i][0]=='C'):
		circuit=line[1:]
		C_list.append(circuit)
	elif(linestring[i][0]=='J'):
		juggler=line[1:4]
		pref=line[4:]
		J_list.append(juggler)
		P_list.append(pref)
	else:
		continue

for i in range(len(C_list)):
	for j in range(len(C_list[i])):	
		if(j<len(C_list[i])-1):
			cfile.write(C_list[i][j]+",")
		else:
			cfile.write(C_list[i][j])
	cfile.write("\n")

for i in range(len(J_list)):
	for j in range(len(J_list[i])):	
		if(j<len(J_list[i])-1):
			jfile.write(J_list[i][j]+",")
		else:
			jfile.write(J_list[i][j])
	jfile.write("\n")
	for k in range(len(P_list[i])):	
		if(k<len(P_list[i])-1):
			pfile.write(P_list[i][k]+",")
		else:
			pfile.write(P_list[i][k])
	pfile.write("\n")

#close all opened files
cfile.close()
jfile.close()
pfile.close()		
