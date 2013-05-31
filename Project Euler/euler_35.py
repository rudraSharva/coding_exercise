# find all the circular primes below a million
# important concepts learned:
# --> all primes are of form (6n-1) or (6n+1)
# --> sweet python string trick to rotate a number

from time import *
start = clock()

# primality test
def isPrime(num):
    for i in range(2,int(num**0.5 +1)):
        if num%i == 0: return 0
    return 1

# main logic
if __name__ == '__main__':
    circularPrimes = []
    array =[i for i in range(10,1000000) if (i+1)%6 == 0 or (i-1)%6 == 0]
    primes = [i for i in array if '0' not in str(i) and '2' not in str(i) and '4' not in str(i) and
             '6' not in str(i) and '8' not in str(i) and isPrime(i)]
    primes.extend([2,3,5,7])

    for number in primes:
        string,flag = str(number),1
        for i in range(1,len(string)):
            if int(string[-i:]+string[:-i]) not in primes:
                flag = 0
                break
        if flag: circularPrimes.append(number)

    print len(circularPrimes)

print "Program Runtime: %.4f seconds" %(clock()-start)