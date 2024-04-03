inpfile=open("input1a.txt","r")
outfile=open("output1a.txt","w")

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

toposort=[]
cyc= [0]* (N+1)
def topo_DFS(start, lst, cyc):
    global toposort,visited
    if cyc[start]==1:
        return "yes"
    cyc[start] = 1
    if lst[start]==0:
        cyc[start] = 2
        return start
    if visited[start]==False:
        visited[start]=True
        for j in lst[start]:
            t=topo_DFS(j, lst, cyc)
            if t=="yes":
                return "yes"
            if t not in toposort:
                toposort.append(t)
            temp= lst[start]
            a= temp[len(temp)-1]
            if j==a:
                cyc[start] = 2
    else:
        cyc[start] = 2
        return start
    return start

visited= [False]* (N+1)
flag=False
for i in range(len(lst)):
    res=topo_DFS(i, lst, cyc)
    if res=="yes":
        flag=True
        break
    if res!=None and res!=0 and res not in toposort:
        toposort.append(res)
toposort.reverse()
if flag==False:
    for i in toposort:
        outfile.write(f"{i} ")
else:
    outfile.write("IMPOSSIBLE")
