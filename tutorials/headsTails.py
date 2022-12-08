def headOrTail(lists):
    h=0
    t=0
    for item in lists:
        if item == 'h':
            h+=1
        else:
            t+=1

#===========
import random
fliplist = []

for i in range(1, 101):
    fliplist += random.choice(['H', 'T'])

print("Heads:", fliplist.count('H'))
print("Tails", fliplist.count('T'))
