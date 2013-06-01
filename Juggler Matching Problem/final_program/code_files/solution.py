'''
*********** Arun Shyam************

Main solution file:

Variable names:
	Circuit_dic: Intial big dictionary, 3 levels deep [format: C[a][b][c] (a=circuit number, b=preference number, c=juggler number)]
		     preference numbers go from 0 to n (0 being highest and n lowest)	

	Main_dic:    Main dictionary in which assignments are made [format: M[a] (a=circuit number): will display all allotments made
		     to that circuit.

        jugglers, preferences and circuits are the files contain the juggler parameters, preferences and circuit parameters resp. 

'''
#import necessary files 
import sys
import string
import re
import heapq
import operator
import collections
import copy

#using alias for heap-max and heap-min
nlarge=heapq.nlargest
nsmall=heapq.nsmallest
itemget=operator.itemgetter(1)

#using Python Autovivification capability 
Circuit_dic=collections.defaultdict(lambda:collections.defaultdict(dict))

#declaring necessary variables
Main_dic={}
Pool=[]
Pool_initial=[]
jugglers = []
preferences = []
circuits = []
juggler_prefer={}
jug_pref={}

#reading necessary files
linestring_1 = open("../input files/juggler.txt", 'r').readlines()
linestring_2 = open("../input files/preferences.txt", 'r').readlines()
linestring_3 = open("../input files/circuit.txt", 'r').readlines()
outfile = open("../output.txt", 'w+')

class writer : 
        def __init__(self, *writers) : 
                self.writers = writers 
        def write(self, text) : 
                for w in self.writers : 
                        w.write(text) 

saveout = sys.stdout
sys.stdout = writer(sys.stdout, outfile)

#converting each read file to a list of vectors
for eachLine in linestring_1:
	line=([int(x) for x in re.split(',',eachLine)])
	jugglers.append(line)
for eachLine in linestring_2:
	line=([int(x) for x in re.split(',',eachLine)])
	preferences.append(line)
for eachLine in linestring_3:
	line=([int(x) for x in re.split(',',eachLine)])
	circuits.append(line)

#an alternate representation for juggler preferences
### lists preferences of circuits for each juggler
for i in range(len(preferences)):
	juggler_prefer[i]=preferences[i][1:]
	jug_pref[i]=preferences[i][:]

#making initial assignments to the big dictionary
## by (circuit number,preference number,juggler)
for i in range(len(jugglers)):
	for j in range(len(preferences[0])):
		Circuit_dic[preferences[i][j]][j][i]=sum(a*b for(a,b) in zip(jugglers[i],circuits[preferences[i][j]]))

#number of jugglers to allocate to each circuit
num_to_allot=len(jugglers)/len(circuits)


#running pass 1 to allocate the most preferred circuits to each juggler 
#keeping in mind the number_to_allocate constraint
"""
Main dictionary contains list of tuples of (juggler,weight) sorted by
weight in decreasing order
--iteritems() iterates over (key,value) pairs of a dictionary
--itemget will sort or get the largest n numbers sorted by the value
-- pool_initial is the common pool storing the remaining jugglers 
-- who cannot be initialized in some circuits
"""
for i in range(len(circuits)):
	if(len(Circuit_dic[i][0])==num_to_allot):
		Main_dic[i]=nlarge(num_to_allot,Circuit_dic[i][0].iteritems(),itemget)
	elif(len(Circuit_dic[i][0])>num_to_allot):
		Main_dic[i]=nlarge(num_to_allot,Circuit_dic[i][0].iteritems(),itemget)
		temp=len(Circuit_dic[i][0])-num_to_allot
		if(temp>1): ##could have used an extend list method instead of conditional loop
			temp_2=nsmall(len(Circuit_dic[i][0])-num_to_allot,Circuit_dic[i][0].iteritems(),itemget)
			for j in range(len(temp_2)):
				Pool_initial.append([temp_2[j]])
		else:		
			Pool_initial.append(nsmall(len(Circuit_dic[i][0])-num_to_allot,Circuit_dic[i][0].iteritems(),itemget))
	else:
		Main_dic[i]=nlarge(len(Circuit_dic[i][0]),Circuit_dic[i][0].iteritems(),itemget)


#allocating the remaining jugglers from pass 1 to a common Pool
# Hence: number of jugglers assigned in pass 1 + Jugglers assigned 
#to pool equals total number of jugglers

## this loop is unnecessary could have been done in the first loop
for i in range(len(Pool_initial)):
		Pool.append(Pool_initial[i][0][0])


#for i in range(len(Main_dic)): print Main_dic[i]

## not needed anyways python default is shallow copy
#make a deep copy of juggler preferences in case we need to use it further
juggler_prefer2 = copy.deepcopy(juggler_prefer)

#Main logic: Keep allocating jugglers to circuits as long as they do not
#violate the max limit per circuit constraint and preference, weight 
#constraints.
while Pool: ## while jugglers are remaining in Pool
	jug=Pool.pop(0)
	jug_list=juggler_prefer2[jug] ##list of preferences of this juggler in terms of circuits
	if(jug_list):
		jug_circuit=jug_list.pop(0)
	else:
		continue
	index=[i for i,x in enumerate(preferences[jug]) if x == jug_circuit] ##get the preference number (will always be in increasing order for a juggler)
	weight_jug=Circuit_dic[jug_circuit][index[0]][jug]
	if(len(Main_dic[jug_circuit])<num_to_allot):
		Main_dic[jug_circuit].append((jug,weight_jug))
		Main_dic[jug_circuit]=sorted(Main_dic[jug_circuit], key=lambda score: score[1], reverse=True) ## or could have used heapify operation
	else:
		wt_circuit=(nsmall(1,Main_dic[jug_circuit],itemget)) ## getting the lowest weight from the circuit
		min_wt_circuit=wt_circuit[0][1] ## could have been done more efficiently using heap or just pulling the last index
		if(weight_jug<min_wt_circuit):
			Pool.append(jug) ## cannot be allocated the preferred circuit (put back in pool)
		else:
			Pool.append(wt_circuit[0][0]) # a better allocation exists, replace existing one and add it to pool)
			Main_dic[jug_circuit]=Main_dic[jug_circuit][:len(Main_dic[jug_circuit])-1]
			Main_dic[jug_circuit].append((jug,weight_jug))
			Main_dic[jug_circuit]=sorted(Main_dic[jug_circuit], key=lambda score: score[1], reverse=True) ## all min-max extraction operations can be simplified by building heap 

#loop for the final display
print "\nFinal Circuit Allotments:\n"
for i in range(len(Main_dic)):
	t1="C"+str(i)
	print t1,
	for j in range(len(Main_dic[i])):
		t2="J"+str(Main_dic[i][j][0])
		print t2,
		for k in range(len(jug_pref[Main_dic[i][j][0]])):
			t3="C"+str(jug_pref[Main_dic[i][j][0]][k])+":"+ str(Circuit_dic[jug_pref[Main_dic[i][j][0]][k]][k][Main_dic[i][j][0]])
			print t3,	
		if(j<len(Main_dic[i])-1):
			print ",",		
	print "\n"
print "\n"
sys.stdout = saveout
outfile.close()

