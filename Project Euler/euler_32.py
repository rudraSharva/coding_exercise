# sum of all numbers that can be written as a sum of pandigital products
from time import *
start = clock()

def pandigitalProd(array,products):
    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            product = array[i]*array[j]
            if ''.join(sorted(str(array[i])+str(array[j])+str(product))) == '123456789':
                if product not in products:
                    products.append(product)
    return products

if __name__ == '__main__':
    products = []
    array = [i for i in range(2,5000) if '0' not in str(i)]
    result = pandigitalProd(array,products)
    print sum(result)

print "Program Runtime: %.2f seconds" %(clock()-start)