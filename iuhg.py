matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
matrix2=[]

for i in range(len(matrix)):
    temp=[]
    for j in range(len(matrix)):
        temp.append(matrix[j][i])
    matrix2.append(temp)
print(matrix2)