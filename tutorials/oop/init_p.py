class Coordinates:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return ""+ str(self.x) + "," + str(self.y)

    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5

def main():
    c = Coordinates(3,4)
    origin = Coordinates(0,0)
    print(c.x)
    print(origin.x)
    print(c.distance(origin))
main()