# pythagorean triplet where a+b+c = 1000

def pythagorean(num):
    result = [a*b*c for a in range(500) for b in range(500) for c in range(500) if c<b<a and a**2 == b**2 + c**2 and a+b+c == num]
    return list(result)

if __name__ == '__main__':
    print pythagorean(1000)