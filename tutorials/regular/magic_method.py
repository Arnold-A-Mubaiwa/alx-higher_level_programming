list =[[4,3,8],[9,5,1],[2,7,6]]
class ProblemALG004r:
    def __init__(self, list, num):
        self.list = list
        self.num =num
    
    def calc(self):
        diag=0
        chk =0  
        tmp_list=[]
        if self.num==2:
            for bott in range(len(self.list)):
                newList = []
                for left in reversed(range(len(self.list))):
                    newList.append(self.list[bott][left])
                print(newList)
        elif self.num == 1:
            for bott in reversed(range(len(self.list))):
                newList = []
                for left in range(len(self.list)):
                    newList.append(self.list[bott][left])
                print(newList)

        for y in range(len(self.list)):
            x_row=0
            y_col=0
            for x in range(len(self.list)):
                x_row +=self.list[x][y]
                y_col += self.list[y][x]
            if  x_row != y_col:
                return False
            diag += self.list[y][y]
            chk += self.list[len(self.list)-y-1][y]
            if diag == chk == x_row == y_col:
                return True
        return False
for i in list:
    print(i)
print(" ")
math_s = ProblemALG004r(list,1)
print(math_s.calc())
math_s1 = ProblemALG004r(list,2)
print(math_s1.calc())