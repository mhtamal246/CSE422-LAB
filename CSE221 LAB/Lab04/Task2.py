import queue
inpfile=open("input2.txt","r")
outfile=open("output2.txt","w")

N=inpfile.readline()
N=N.split(" ")

node=int(N[0])
edge=int(N[1])

lstt=[0]*(node+1)

start,end=inpfile.readline().split(" ")
start=int(start)
lstt[start]=[start,int(end)]

for i in range(edge-1):
    line=inpfile.readline()
    line=line.split(" ")
    lst=[]
    num=int(line[1])
    lst.append(num)

    if lstt[int(line[0])]==0:
        lstt[int(line[0])]=lst
    else:
        lstt[int(line[0])].append(num)

print("Adjacency: ",lstt)

visited=[False]*(node+1)

qu = queue.Queue()
qu.put(start)
final=[]
while not qu.empty():
    cur = qu.get()
    if visited[cur] == False:
        final.append(cur)
        visited[cur] = True
        if lstt[cur]!=0:
            for i in lstt[cur]:
                if visited[i] == False:
                    qu.put(i)
print("BFS: ",final)