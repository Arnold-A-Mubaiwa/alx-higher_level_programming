#3! = 3 * 2* 1

def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n-1)
        return result

print(factorial(4))