# Maximum adjacent number sum down the triangle.
# think simple, think hard, conquer.

from time import *
start = clock()

# return the maximum sum going down
def maxSum(array):
    i,maxTillNow = 1,{0:array[0]}
    for j in range(1,len(array)):
        k = i*(i+1)/2
        if j == k:
            maxTillNow[j] = maxTillNow[j-i]+array[j]
        elif j == k+i:
            maxTillNow[j] = maxTillNow[j-(i+1)]+array[j]
            i +=1
        else:
            maxTillNow[j] = max((maxTillNow[j-i]+array[j]),(maxTillNow[j-(i+1)]+array[j]))
    return max(maxTillNow.values())

# main
if __name__ == '__main__':
    f = open('triangle.txt')
    array   = [int(i) for i in f.read().split()]
    print maxSum(array)

print "Program Runtime: %.4f seconds" %(clock()-start)