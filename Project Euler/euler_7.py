import math
import itertools

# itertools.count used for getting infinite stream of numbers
# find 10001 st prime number

def primality(n):
    count = 0
    flag = 1
    for num in itertools.count(2,1):
        for i in range(2,int(math.sqrt(num))+1):
            if num%i ==0:
                flag = 0
                break
        if flag:
            count +=1
        else:
            flag = 1
        if count == n:
            print num
            break

if __name__ == '__main__':
    primality(10001)







