oneToTen = range(1, 11)

def dbl_num(num):
    return num * 2

print(list(map(dbl_num,oneToTen)))


print(list(map(lambda x: x * 3, oneToTen)))

alist = (list(map(lambda x, y: x + y, [1,2,3], [1,2,3])))
print(alist)

print(list(filter(lambda x: x % 2 == 0, oneToTen)))
