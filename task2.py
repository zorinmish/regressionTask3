#n, m = map(int, input("Write N and M:").split())
n, m = map(int, input().split())


matrix = [[0]*m]*n
adj_list = {}
used = [0]*(n*m)
result = 0

def mn(i,j, M = m):
    return i*M+j

def graph():
  for node in adj_list:
    print(node, " ---> ", [i for i in adj_list[node]])
    
def dfs(v):
    used[v] = 1
    #print(v)
    temp = adj_list[v]
    for i in temp:
        if used[i] == 0:
            dfs(i)

for i in range(n):
    matrix[i] = list(map(int, input().split()))
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            temp = []
            if mn(i-1, j)>=0:
                if matrix[i-1][j] == 1:
                    temp.append(mn(i-1, j))
                    
            if j>0:
                if matrix[i][j-1] == 1:
                    temp.append(mn(i, j-1))
                    
            if j<m-1:
               if matrix[i][j+1] == 1:
                    temp.append(mn(i, j+1)) 
                    
            if mn(i+1, j)<n*m:
                if matrix[i+1][j] == 1:
                    temp.append(mn(i+1, j))
                    
            adj_list[mn(i,j)] = temp

#graph()

for key in adj_list.keys():
    if used[key] == 0:
        result+=1
        dfs(key)
        
print(result)
#print("Total amount of islands: ", result)