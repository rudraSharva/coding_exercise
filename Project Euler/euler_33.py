# find all the fractions with unorthodox cancelling method

from time import *
start = clock()

# main
if __name__ == '__main__':
    product_i, product_j = 1, 1
    array = [(i,j) for i in range (10,100) for j in range(10,100) if j>i and set(str(i)).intersection(set(str(j)))
                                                                     and i%10!=0 and j%10 !=0]
    for (i,j) in array:
        inter = list(set(str(i)).intersection(set(str(j))))[0]
        a,b = list(str(i)),list(str(j))
        a.remove(inter)
        b.remove(inter)
        if float(i)/j == float(a[0])/float(b[0]):
            product_i *= i
            product_j *= j

    print product_j/product_i

print "Program Runtime: %.4f seconds" %(clock()-start)