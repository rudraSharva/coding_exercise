# sum of didts in 2^1000

def find_sum(num):
    total = 0
    while num:
        digit = num%10
        num /= 10
        total += digit
    return total

if __name__ == '__main__':
    print find_sum(2**1000)