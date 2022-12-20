#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    # try:
    #     my_list_1[list_length-1]
    #     my_list_2[list_length-1]
    new_list = []
    for i in range(0, list_length):
        num = 0
        try:
            num = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("divide by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(num)
    return new_list

my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)