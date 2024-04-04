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

for i in range(1, len(lst)):
    if lst[i]==0:
        lst[i]=[i]

rev=[0]* (N+1)
for i in range(len(lst)):
    if lst[i]!=0:
        idx=lst[i]
        for j in idx:
            if rev[j]!=0:
                rev[j].append(i)
            else:
                rev[j]=[i]

visited=[False]* (N+1)
ref=[]
def SCC1(start, lst, visited):
    global ref
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
def SCC2(start, rev, visited):
    global scc, ls
    if visited[start]==False:
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
