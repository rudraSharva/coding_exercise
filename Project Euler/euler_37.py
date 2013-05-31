# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

from time import *
start = clock()

def prime(num):
    for i in range(2,int(num**0.5)+1):
        if num%i == 0: return 0
    return 1

if __name__ == '__main__':
    result = []
    numbers = [num for num in range(11,1000000) if (num+1)%6 == 0 or (num-1)%6 == 0]
    seived  = [i for i in [num for num in numbers if str(num)[0] in ['2','3','5','7'] and str(num)[-1] in ['3','7']] if prime(i)]
    print len(seived)
    for i in seived:
        num = str(i)
        a1 = [num[:j+1] for j in range(len(num)-1)]
        a2 = [num[j+1:] for j in range(len(num)-1)]
        a2.extend(a1)
        if len([0 for number in a2 if prime(int(number))==0]) is 0: result.append(int(num))
    print sum(result)

print "Program Runtime: %.4f seconds" %(clock()-start)