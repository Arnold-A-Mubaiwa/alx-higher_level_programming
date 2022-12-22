class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name

u = User()
print(u.id)
print(u.is_new)
print(u.name)

u = User("John")
print(u.name)
print(u.__password)