import queue

inpfile=open("input3.txt","r")
outfile=open("output3.txt","w")

N,M=inpfile.readline().split(" ")
N,M=int(N),int(M)

lst=[0]* (N+1)

for i in range(M):
    a,b,w=inpfile.readline().split(" ")
    a,b,w=int(a),int(b),int(w)

    if lst[a]==0:
        lst[a]=[(b,w)]
    else:
        lst[a].append((b,w))


start=1
dij_lst=[float('+inf')]* (N+1)
qu=queue.Queue()
qu.put(start)
visited=[False]* (N+1)
minlst=[]
dij_lst[start]=0
while not qu.empty():
    cur=qu.get()
    visited[cur]=True
    if lst[cur]!=0:
        for i in lst[cur]:
            des,weight=i
            if weight<dij_lst[cur]:
                dij_lst[des]=dij_lst[cur]
                minlst.append(dij_lst[des])
            else:
                dij_lst[des]=weight
                minlst.append(dij_lst[des])
    minlst.sort()
    if len(minlst)>0:
        mini=minlst.pop(0)
        for i in range(len(dij_lst)):
            if dij_lst[i]==mini:
                idx=i
        qu.put(idx)

outfile.write(f"{dij_lst[len(dij_lst)-1]}")

inpfile.close()
outfile.close()