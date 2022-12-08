def multi_by_2(num):
    return num * 2

times_two = multi_by_2

print("4 * 2 =", times_two(4))

def do_math(func, num):
    return func(num)

print("8 * 2 = ", do_math(multi_by_2, 8))

# ============================

def get_func_mult_by_num(num):
    print("num is ",num)
    def multi_by(value):
        print("value is ", value)
        return value * num
    
    return multi_by

generated_func = get_func_mult_by_num(5)

print("5 * 10 = ", generated_func(10))

listOfFuncs = [times_two, generated_func]
print(listOfFuncs[1](9))