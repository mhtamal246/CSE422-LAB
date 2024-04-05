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
        lst[a].append(b)   #this part will create the adjacency list

toposort=[]
cyc= [0]* (N+1)
def topo_DFS(start, lst, cyc):
    global toposort,visited
    if cyc[start]==1:               #to detect cycle we used a list of 0,1,2
        return "yes"                #when the vertices is being visited then it will become 0 to 1 and when if fully explored or backtracking then it will become 2
    cyc[start] = 1                  #if that doesn't backtrack and find a cyc[value] with 1 then we can say that there is a loop
    if lst[start]==0:
        cyc[start] = 2              #using dfs to do topological sort, we can pick any node, then start the dfs, when it reaches to the end then it will start backtracking
        return start                #when it backtracks, that value is actually the last value of a particaular sequence. if we store that in a list and we will find a topo-sort
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

inpfile.close()
outfile.close()