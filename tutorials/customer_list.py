customers = []

def enterCustomer():
    cname, csname = input("Enter Customer Name: ").split()
    customers.append({"cname":cname, "csname":csname})
    return customers

while (True):
    q = input("Enter Customer (YES/NO): ").lower()
    if q == 'yes' or q == 'y':
        enterCustomer()
    else:
        break
        
for c in customers:
    print(c)