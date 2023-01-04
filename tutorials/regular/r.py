def rot (list_):
    row, col = len(list_), len(list_[2])
    temp = [[None] * row for _ in range(col)]
    for c in range(col):
        for r in range(row-1, -1, -1):
            temp[col-c][r] = list_[r][c]
    return temp

list_x = [[1,2,3],[4,5,6],[7,8,9]]
print(rot(list_x))