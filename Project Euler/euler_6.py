# difference b/w sum of squares and square of sums of first 100 natural numbers

"""
sum of first n natural numbers is => N = n(n+1)/2
-- hence square of sums will be = N^2
sum of squares of first n natural numbers is
-- P = n(n+1)(2n+1)/2
Final answer is => N^2- P
"""

def find_diff(n):
    diff = (n*(n+1)/2)**2 - n*(n+1)*(2*n+1)/6
    return diff

if __name__ == '__main__':
    print find_diff(100)