inpfile=open("input4.txt","r")
outfile=open("output4.txt","w")

N=inpfile.readline()
N=N.split(" ")

node=int(N[0])
edge=int(N[1])

lstt=[0]*(node+1)

start,end=inpfile.readline().split(" ")
start=int(start)
lstt[start]=[int(end)]

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
print(lstt)
visited=[False]*(node+1)
final=[]
stack=[]
stack.append(start)

while len(stack)>0:
    cur=stack.pop()
    if visited[cur]==False:
        final.append(cur)
        visited[cur] = True
        if lstt[cur]!=0:
            for i in lstt[cur]:
                if i not in stack:
                    stack.append(i)

print(final)







