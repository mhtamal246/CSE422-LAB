import queue

inpfile=open("input2.txt","r")
outfile=open("output2.txt","w")

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

B,A=inpfile.readline().split(" ")
B,A=int(B),int(A)
visited=[False]* (N+1)
def bob(lst,visited,B):
    qu = queue.Queue()
    qu.put(B)
    boblst = [float('inf')] * (N + 1)
    minlst = []
    boblst[B] = 0
    while not qu.empty():
        cur = qu.get()
        visited[cur] = True
        if lst[cur] != 0:
            for i in lst[cur]:
                des, weight = i
                if boblst[des] == float('+inf'):
                    boblst[des] = boblst[cur] + weight
                    minlst.append(boblst[des])
                else:
                    if boblst[cur] + weight < boblst[des]:
                        boblst[des] = boblst[cur] + weight
                        minlst.append(boblst[des])
        minlst.sort()
        if len(minlst) > 0:
            mini = minlst.pop(0)
            for i in range(len(boblst)):
                if boblst[i] == mini:
                    idx = i
                    break
            qu.put(idx)

    return boblst

bo=bob(lst,visited,B)

def alice(lst,A):
    qu = queue.Queue()
    qu.put(A)
    allst = [float('inf')] * (N + 1)
    minlst = []
    allst[A] = 0
    while not qu.empty():
        cur = qu.get()
        if lst[cur] != 0:
            for i in lst[cur]:
                des, weight = i
                if allst[des] == float('+inf'):
                    allst[des] = allst[cur] + weight
                    minlst.append(allst[des])
                else:
                    if allst[cur] + weight < allst[des]:
                        allst[des] = allst[cur] + weight
                        minlst.append(allst[des])
        minlst.sort()
        if len(minlst) > 0:
            mini = minlst.pop(0)
            for i in range(len(allst)):
                if allst[i] == mini:
                    idx = i
                    break
            qu.put(idx)

    return allst

al=alice(lst,A)
time=float("inf")
node=0
for i in range(1,len(bo)):
    if bo[i]!=float('inf') and al[i]!=float('inf'):
        if bo[i]<time and al[i]<time:
            if bo[i]>al[i]:
                time=bo[i]
            else:
                time=al[i]
            node=i


if time==float('inf'):
    outfile.write("Impossible")
else:
    outfile.write(f"Time {time}\nNode {node}")
print(time)
print(node)
print(bo)
print(al)