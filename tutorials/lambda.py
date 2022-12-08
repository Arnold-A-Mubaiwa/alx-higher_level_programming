sum = lambda x, y: x + y
print(sum(4,5))

can_vote = lambda age: True if age >= 18 else False
print(can_vote(18))

power_list = [lambda x: x**2, lambda x: x**3, lambda x: x**4]
for func in power_list:
    print(func(5))

attack = {  'quick':(lambda: print("Quick Attack")),
            'power':(lambda: print("Power Attack")),
            'miss':(lambda: print("Missed Attack"))
        }
attack['quick']()
import random
attackkey = random.choice(list(attack.keys()))
attack[attackkey]()

