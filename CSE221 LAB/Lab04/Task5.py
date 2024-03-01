import queue
inpfile=open("input5.txt","r")
outfile=open("output5.txt","w")

N=inpfile.readline()
N=N.split(" ")

node=int(N[0])
edge=int(N[1])


lstt=[0]*(node+1)

start,end=inpfile.readline().split(" ")
start=int(start)
lstt[start]=[int(end)]
lstt[int(end)]=[int(start)]

for i in range(edge-1):
    line=inpfile.readline()
    line=line.split(" ")
    num1=int(line[0])
    num2=int(line[1])

    if lstt[num1]==0:
        lstt[num1]=[num2]
    else:
        if num2 not in lstt[num1]:
            lstt[num1].append(num2)

    if lstt[num2]==0:
        lstt[num2]=[num1]
    else:
        if num1 not in lstt[num2]:
            lstt[num2].append(num1)

start=1  #always starts at city 1
des=int(N[2])
visited=[False]*(node+1)
qu = queue.Queue()
qu.put(start)
distance=[]
visited[start]=True
parent=[-1]*(node+1)
parent[start]=-1

while not qu.empty():
    cur = qu.get()
    for i in lstt[cur]:
        if visited[i]==False:
            visited[i]=True
            parent[i]=cur
            qu.put(i)
c=des
path=[]
path.append(c)
time=0
while c!=start :
    c=parent[c]
    path.append(c)
    time+=1
path.reverse()

stg=""
for i in path:
    stg+=str(i)+" "

outfile.write(f"Time: {time}\n")
outfile.write(f"Shortest Path: {stg[:len(stg)-1]}")
