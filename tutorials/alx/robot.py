class Robot:
    def __init__(self, name=None):
        self.name = name
    
    def say_hi(self):
        if self.name:
            print("Hi, I am "+ self.name)
        else:
            print("Hi, I am a robot without a name")
    
    def set_name(self, name):
        self.name = name
    
    def get_name(self):
        return self.name

x = Robot()
x.say_hi()
x.set_name("Arnold")
x.say_hi()
print(x.get_name())