def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

def check_if_odd(fun, list_=[]):
    b = []
    for item in list_:
        b.append(fun(item))
    return b

a = [1,2,6,9,88,4,1,2,6,89,5,4,3]
print(check_if_odd(is_odd, a))

# ===================================
