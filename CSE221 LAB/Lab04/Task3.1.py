
inpfile=open("input3.txt","r")
outfile=open("output3.txt","w")

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
            c=lstt[cur]
            for i in range(len(c)-1,-1,-1):
                stack.append(c[i])

print(final)



inpfile.close()
outfile.close()