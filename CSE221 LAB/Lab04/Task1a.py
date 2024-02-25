import numpy as np
inpfile=open("input1a.txt","r")
outfile=open("output1a.txt","w")

V,E=inpfile.readline().split(" ")
V=int(V)
E=int(E)
arr=np.zeros((V+1,V+1), dtype=int)

for steps in range(E):
    s=inpfile.readline()
    s=s.split(" ")
    l=[]
    for i in s:
        l.append(int(i))
    r=l[0]
    c=l[1]
    w=l[2]
    row,col=arr.shape
    for i in range(row):
        for j in range(col):
            if i==r and j==c:
                arr[i][j]=w

outfile.write(f"{arr}")
inpfile.close()
outfile.close()