# largest palindrome formed by two 3 digit numbers

def palindrome(num):
    total ,number = 0, num
    while num:
        digit = num%10
        num /= 10
        total = total*10+digit
    if total == number:
        return 1

def max_length_palindrome():
    result = [i*j for i in range(100,1000) for j in range(100,1000) if palindrome(i*j)]
    print max(result)
    
if __name__ == '__main__':
    max_length_palindrome()