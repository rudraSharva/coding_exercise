# sum of even terms of a fibonacci sequence not exceeding 4,000,000

def fibo(n):
    a,b = 0,1
    while a<=n:
        yield a
        c = a
        a += b
        b = c

x = sum( i for i in fibo(4000000) if i%2==0)
print x