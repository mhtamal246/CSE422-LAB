import numpy as np
inpfile = open('input6.txt', 'r')
outfile= open('output6.txt', 'w')

r, c = inpfile.readline().split(' ')
r, c = int(r), int(c)
arr = np.zeros((r,c), dtype = 'str')
for i in range (r):
    temp = inpfile.readline()
    if i!= (r-1):
        temp = temp[0:len(temp)-1]
    for j in range (c):
        arr[i][j] = temp[j]

Count = 0
CurMax = 0
def dfs(i, j, prevColor, newColor):
    global CurMax
    if i<0 or i>r-1 or j<0 or j>c-1 or arr[i][j] == newColor or arr[i][j] not in prevColor:
        return
    if arr[i][j] == 'D':
        CurMax+=1
    arr[i][j] = newColor
    dfs(i+1, j,prevColor, newColor)
    dfs(i-1, j,prevColor, newColor)
    dfs(i, j+1,prevColor, newColor)
    dfs(i, j-1,prevColor, newColor)

path = ['D','.']
for i in range (r):
    for j in range (c):
        if arr[i][j] in path:
            dfs(i, j, path, 'W')
            if CurMax>Count:
                Count = CurMax
            CurMax = 0

outfile.write(f"{Count}")

inpfile.close()
outfile.close()