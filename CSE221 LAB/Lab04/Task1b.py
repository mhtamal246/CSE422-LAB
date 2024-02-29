import numpy as np
inpfile=open("input1b.txt","r")
outfile=open("output1b.txt","w")

N=inpfile.readline()
N=N.split(" ")

node=int(N[0])
edge=int(N[1])

lstt=[0]*(node+1)
for i in range(edge):
    line=inpfile.readline()
    line=line.split(" ")
    lst=[]
    tup=(int(line[1]),int(line[2]))
    lst.append(tup)

    if lstt[int(line[0])]==0:
        lstt[int(line[0])]=lst
    else:
        lstt[int(line[0])].append(tup)
count=0
for i in range(len(lstt)):
    if lstt[i]==0:
        outfile.write(f"{count}:\n")
        count+=1
    else:
        stg=""
        for j in str(lstt[i]):
            stg+=j
        outfile.write(f"{count}: {stg[1:-1]}\n")
        count+=1

inpfile.close()
outfile.close()