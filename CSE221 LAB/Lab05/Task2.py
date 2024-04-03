import heapq
inpfile=open("input2.txt","r")
outfile=open("output2.txt","w")

N,M=inpfile.readline().split(" ")
N,M=int(N),int(M)

lst=[0]* (N+1)

for i in range(M):
    a,b=inpfile.readline().split(" ")
    a,b=int(a),int(b)

    if lst[a]==0:
        lst[a]=[b]
    else:
        lst[a].append(b)
indeg=[0]* (N+1)
for i in lst:
    if i!=0:
        for j in i:
            indeg[j]+=1

data=[]
visited=[False]* (N+1)
toposort=[]
for i in range(1,len(indeg)):
    if indeg[i]==0:
        data.append(i)

while len(data)>0:
    heapq.heapify(data)
    q= data.pop(0)
    if visited[q]==False:
        toposort.append(q)
        visited[q]=True
        if lst[q]!=0:
            for i in lst[q]:
                indeg[i]-=1
                if indeg[i]==0:
                    data.append(i)


if len(toposort)!=N:
    outfile.write("IMPOSSIBLE")
else:
    for i in toposort:
        outfile.write(f"{i} ")