inpfile= open("input1.txt","r")
outfile= open("outfile1.txt","w")

ppl, qu= inpfile.readline().split(" ")
ppl, qu= int(ppl), int(qu)

def find(parent, val):
    if parent[val]==val:
        return val
    else:
        return find(parent,parent[val])


def DSU(parent,n1,n2):
    r1=find(parent,n1)
    r2=find(parent,n2)
    if r1!=r2:
        parent[r2]=r1
        size[r1]+=size[r2]

parent=[-1]*ppl
size=[1]*ppl
for i in range(ppl):
    parent[i]=i
for i in range(qu):
    n1,n2=inpfile.readline().split(" ")
    n1,n2= int(n1),int(n2)
    DSU(parent, n1,n2)
    count=size[find(parent,n1)]
    outfile.write(f"{count}\n")