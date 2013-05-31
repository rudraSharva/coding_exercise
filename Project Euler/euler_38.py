# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product
# of an integer with (1,2, ... , n) where n >1?

from time import *
start = clock()

# finding the maximum (remove the string with duplicates,containing 0 or less than len 9
def max_pandigital(array,maximum):
    for num in array:
        numStr = str(num*1)+str(num*2)
        if len(set(list(numStr))) == 9:
            if '0' not in numStr and int(numStr) > maximum:
                maximum = int(numStr)
    return maximum

# need to check only 9000 to 10000 range
# Reasons:
# 1). we already know that maximum number has to be bigger or equal to 9 pandig.
# 2). this range will be multiplied by (1,2) to yeild number of 9 dig long.
# not true with (90 - 99) when mult. with (1,2,3), we get num greater than
# 9 digit long, so eliminate them.
if __name__ == '__main__':
    maximum = 918273645 # pandigital of 9 * (1..5) as given in question
    array = [i for i in range(9000,10000) if '0' not in str(i)]
    result = max_pandigital(array,maximum)
    print result

print "Program Runtime: %.4f seconds" %(clock()-start)