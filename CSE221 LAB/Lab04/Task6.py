import numpy as np
inpfile=open("input6.txt","r")
outfile=open("output6.txt","w")

row,col=inpfile.readline().split(" ")
row,col=int(row),int(col)

arr=np.zeros((row,col),dtype=str)

def helper(lst,r,c=0):
      for val in lst:
            arr[r][c]=val
            c+=1
for i in range(row):
      lst=[]
      n=inpfile.readline()
      for j in n:
            lst.append(str(j))
      helper(lst[:-1],i)

count=[]
for i in range(row):
      for j in range(col):
            if arr[i][j]=="." or arr[i][j]=="D":
                  if arr[i]==1:

def DFS(left,right,up,down):
