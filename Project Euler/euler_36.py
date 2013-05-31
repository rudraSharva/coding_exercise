# Find the sum of all numbers less than one million, which are palindromic in base 10 and base 2.

from time import *
start = clock()

# find palindrome
def palindrome(string):
    if string == string[::-1]:
        return 1

# recursive binary representation of a number
def binary(num):
    if num in [0,1]: return str(num)
    return binary(num/2) + str(num%2)

if __name__ == '__main__':
    print sum([num for num in range(1,1000000) if num%2!=0 and palindrome(str(num)) and palindrome(binary(num))])

print "Program Runtime: %.4f seconds" %(clock()-start)