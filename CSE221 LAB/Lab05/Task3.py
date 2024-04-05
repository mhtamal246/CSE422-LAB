inpfile=open("input3.txt","r")
outfile=open("output3.txt","w")

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

for i in range(1, len(lst)):     #this part will find if there's any node that is disconnected singly nodes
    if lst[i]==0:                  #if there is then it will put that node into the adjacency list
        lst[i]=[i]

rev=[0]* (N+1)
for i in range(len(lst)):
    if lst[i]!=0:                   #this part will change the direction of the edges
        idx=lst[i]                  #if there's a node going 1 to 3 then this part will create another reverse list that is going 3 to 1
        for j in idx:
            if rev[j]!=0:
                rev[j].append(i)
            else:
                rev[j]=[i]

visited=[False]* (N+1)
ref=[]
def SCC1(start, lst, visited):          #in the part dfs call we will traverse normally using dfs
    global ref                          #when traversing we will put current node into a ref list which is our reference list
    if visited[start]==False:
        visited[start]=True
        ref.append(start)
        if lst[start]!=0:
            for i in lst[start]:
                SCC1(i,lst,visited)

for i in range(1, len(lst)):
    SCC1(i,lst,visited)
ref.reverse()
visited=[False] * (N+1)
scc=[]
ls=[]
def SCC2(start, rev, visited):          #2nd time we will pop a node from the reference list and perform a dfs at that reverse list
    global scc, ls                      #while traversing we will create a list of list where we will put the SCCs
    if visited[start]==False:           # while traversing if we reach to the dead-end then we can say that till that portion we have our 1 strongly connected part
        visited[start]=True
        ls.append(start)
        if rev[start]!=0:
            for i in rev[start]:
                SCC2(i, rev, visited)
        ls.sort()
        scc.append(ls)
        ls=[]

r=len(ref)
for i in range(r):
    start=ref.pop()
    SCC2(start, rev, visited)

for i in scc:
    if len(i)>0:
        for j in i:
            outfile.write(f"{j} ")
        outfile.write(f"\n")

inpfile.close()
outfile.close()