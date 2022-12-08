# dic = {"name":"Arnold", "age":19}

# print("My name :", dic["name"])
# print("name" in dic)
# print(dic.values())

# for v in dic.values():
#     print(v)

# print(len(dic))

fname, sname = input("Enter your name and surname: ").split()
employee = []
employee.append({"fname":fname, "sname":sname})
print(employee)