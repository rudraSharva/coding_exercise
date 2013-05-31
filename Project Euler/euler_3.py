import math
import itertools

# largest prime factor of a composite number
def primality(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i ==0:
            return 0
    return 1

if __name__ == '__main__':
    number = 600851475143
    for i in itertools.count(2,1):
        if number%i == 0:
            if number%10 in [7,9,1,3] and primality(number/i):
                print number/i
                break

