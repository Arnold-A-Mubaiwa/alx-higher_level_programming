from file_two import function_three

print("file one __name__ is set to: {}".format(__name__))

def function_one():
    print("Function 1 is executed")

def function_two():
    print("Function 2 is executed")

if __name__ == '__main__':
    print("file one executed when ran directly")
    function_two()
    function_three()
else:
    print("file one executed when imported")