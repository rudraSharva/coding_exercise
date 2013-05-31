# lcm of first 20 natural numbers

def lcm(num1,num2):
    d, s = 2, 1
    while d<=num1 and d<=num2:
        if num1%d == 0 and num2%d == 0:
            s *= d
            num1,num2 = num1/d,num2/d
        else:
            d +=1
    return s*num1*num2

if __name__ == '__main__':
    print reduce(lcm, range(1,21))
