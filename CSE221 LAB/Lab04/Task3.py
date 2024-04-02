
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
def DFS(start, visited, lstt, final=[]):
    if lstt[start]!=0:
        if visited[start]==False:
            visited[start]=True
            final.append(start)
            for i in lstt[start]:
                DFS(i,visited,lstt,final)

    return final

fin=DFS(start,visited,lstt,final)

for i in fin:
    outfile.write(f"{i} ")

inpfile.close()
outfile.close()