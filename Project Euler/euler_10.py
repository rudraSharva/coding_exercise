import math
import itertools

# find sum of first 2 Million prime numbers
# tip - eliminate even numbers

def sum_primes(n):
    sum = 0
    count = 0
    flag = 1
    for num in itertools.count(2,1):
        if num%2 == 0:
            continue
        for i in range(2,int(math.sqrt(num))+1):
            if num%i ==0:
                flag = 0
                break
        if flag and num < n:
            count +=1
            sum += num
        else:
            flag = 1
        if num > n:
            break
    return sum
if __name__ == '__main__':
    print sum_primes(2000000)







