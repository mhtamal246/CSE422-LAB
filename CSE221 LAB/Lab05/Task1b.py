import queue
inpfile=open("input1b.txt","r")
outfile=open("output1b.txt","w")

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
    if i!=0:                       #this part will create a list of those node having 0 indegre edge
        for j in i:
            indeg[j]+=1

Q=queue.Queue()
visited=[False]* (N+1)
toposort=[]                         #in this part we will put all the node with 0 indegree into a queue
for i in range(1,len(indeg)):
    if indeg[i]==0:
        Q.put(i)

while not Q.empty():
    q=Q.get()                       #then we will take a node and start our bfs traversal.
    if visited[q]==False:           #while visiting a node we will minus 1 of its child node's indegree
        toposort.append(q)          #after that if any node becomes 0 [indegree] then we will put that into the queue
        visited[q]=True
        if lst[q]!=0:
            for i in lst[q]:
                indeg[i]-=1
                if indeg[i]==0:
                    Q.put(i)

if len(toposort)!=N:               #after the bfs if there is a cycle then there's no way the bfs will run till the end
    outfile.write("IMPOSSIBLE")     # so there will be less vertices in the topo list than actual number of vertices
else:                               #this means the topo sort is impossible because of the cycle.
    for i in toposort:
        outfile.write(f"{i} ")

inpfile.close()
outfile.close()