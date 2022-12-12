class RotateArrays:

    def __init__(self, rotation, listT):
        self.rotation = rotation
        self.listT = listT

    def rot(self):
        newTemp = self.listT
        for i in range(self.rotation):
            row, col = len(newTemp), len(newTemp[0])
            temp = [[None] * row for _ in range(col)]
            for c in range(col):
                for r in range(row-1, -1, -1):
                    temp[col-c-1][r] = newTemp[r][c]
            newTemp = temp
        return temp
        
    def rotate(self):
        if self.rotation == 0:
            return self.listT
        else:
            return self.rot()
        
def main():
    list_x = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
    for x in range(10):
        n = RotateArrays(x, list_x).rotate()
        for i in n:
            print(i)
        print()

main()