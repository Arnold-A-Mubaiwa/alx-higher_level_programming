list_x = [[1,2,3],[4,5,6],[7,8,9]]
temp=[]
temp_2=[]
len_ = len(list_x)-1

temp = list_x
for  x in range(0, len(list_x)):
    for i in list_x[x]:
        if len_ == -1:
            break
        for j in range(len_,-1, -1):
            temp[x][j] = i
print(temp)
