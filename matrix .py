distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
path=[0,1,2,3]
total=0
for i in range(len(path)-1):
    total += distance_matrix[path[i]][path[i+1]]
    print(total)
total+=distance_matrix[path[-1]][path[0]]
print(total)