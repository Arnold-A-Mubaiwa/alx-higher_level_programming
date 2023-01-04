print("file two __name__ is set to: {}".format(__name__))

def function_three():
    print("Function 3 is executed")

def function_four():
    print("Function 4 is execcuted")

if __name__ == "__main__":
    print("file two executed when ran directly")
else:
    print("File two executed when imported")