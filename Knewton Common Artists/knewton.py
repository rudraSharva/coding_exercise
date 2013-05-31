#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Requirements:
    Python 2.7,no external package or dependency.
To Run:
    On command prompt: "python knewton.py" (braces excluded)
    The program does not take any command line arguments. Please specify the path
    to artist file in the params.cfg file under config folder.

Complexity analysis:
    The complexity can be calculated in following manner:
    Time complexity is comprised of basically 2 processing functions.
      artistUserMapping:
       Here the complexity is O(M*L) [M is number of users,L is avg.
                                      length of the preference list]
      findPairs:
       Here there are two loops.
        loop 1. Complexity O(N) [N is number of unique artists]
        loop 2. Complexity O(T)[filtered artists] ~O(N) [in the worst case]
        combination step(finding artist pairs) : O(T^2)

    Overall complexity : O(M*L)+2*O(N)+O(T^2) ~ O(M*L)+O(T^2)
    The running time can depend a lot on T. If T approach N then
    depending on N the runtime of program can increase significantly

    There is another approach of having keys as artists pair instead of
    indivisual artist and return the qualifying artists. The runtime there
    will be O(N*L*M). The time in seconds that took when I tried that approach
    was '2.05' sec on my machine. But if the list is representative of real
    world scenario then the minor tweaks that I did can go a long way in
    improving the runtime of the program.

    This program runs under 80 ms (0.076 s) on my machine. At present I am
    content with it but there might be many alternatives available who handle
    the worst cases better.

    One good technique would be to use Genetic Algorithms which through mutation
    and crossover over time will become more optimal.As the runtime already is under
    1/10th of a second any drastic optimization or paradigm might be an overkill.

@author - Arun Shyam
@date - 05/03/2013
"""

import sys,os
import ConfigParser
from time import clock
from itertools import combinations
from collections import defaultdict

def getConfig():
    """
    Read params configuration file
    Parameters:
      none
    """
    cwd = os.getcwd()
    config = ConfigParser.ConfigParser()
    config.read(cwd +'/config/params.cfg')
    return config

def readFile(artist_file):
    """
    read the input artist file
    Parameters:
      artist_file -> input user preference file
    Returns:
      a file handler
    """
    try:
        fp = open(artist_file,'r')
        return fp
    except IOError:
        print 'cannot open file:', artist_file, '...exiting'
        sys.exit()

def artistUserMapping(fp,artist_user_dict):
    """
    Maps the artist to the users:
     Parameters:
       fp -> open file handle
       artist_user_dict -> defaultdict(set) construct
                           maps unique artists to all
                           users who like it.
     Returns:
       none
    """
    user = 1 # total of 1000 users
    for line in (fp.readlines()):
        line = line.split(',')
        for artist in line:
            artist_user_dict[artist].add(user)
        user +=1
    fp.close()

def findPairs(artist_user_dict,threshold):
    """
    Main logic: returns the desired artist pairs.
    Idea is that to have threshold number of users
    common b/w artists, the artist should atleast
    appear threshold number of times in user list>
    This cuts down the processing a lot.
      Parameters:
        artist_user_dict -> defaultdict(set) construct
                            maps unique artists to all
                            users who like it.
        threshold -> minimum no. of common users needed.
      Returns:
        result -> final result (artist pairs)
    """
    result,relevant_artists = [],[]
    for key in artist_user_dict: #
        if len(artist_user_dict[key]) >= threshold:
            relevant_artists.append(key)
    artist_pairs = combinations(relevant_artists,2)
    for i,j in artist_pairs:
        if len(artist_user_dict[i].intersection(artist_user_dict[j])) >= threshold:
            result.append((i,j))
    return result

if __name__ == '__main__':
    start = clock() #time starts here
    config = getConfig() # return config handler
    threshold = config.getint('parameters','THRESHOLD') #the number
    artist_file = config.get('parameters','PATH') # artist file location
    artist_user_dict,fp = defaultdict(set),readFile(artist_file)
    artistUserMapping(fp,artist_user_dict)
    result = findPairs(artist_user_dict,threshold)
    for i,j in result:
        print i,',',j
    #print "Program Runtime: %.4f seconds" %(clock()-start) # runtime in seconds