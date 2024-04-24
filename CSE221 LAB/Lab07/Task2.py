inpfile= open("input2.txt","r")
outfile= open("output2.txt","w")

ppl, qu= inpfile.readline().split(" ")
ppl, qu= int(ppl), int(qu)

def find(parent, val):
    if parent[val]==val:
        return val
    else:
        return find(parent,parent[val])


def DSU(parent,n1,n2, wgt):
    global count
    r1=find(parent,n1)
    r2=find(parent,n2)
    if r1!=r2:
        parent[r2]=r1
        count+=wgt

count= 0
parent=[-1]* (ppl+1)
lst=[]
for i in range(ppl):
    parent[i]=i
for i in range(qu):
    n1,n2,wgt=inpfile.readline().split(" ")
    n1,n2,wgt= int(n1),int(n2),int(wgt)
    lst.append((n1,n2,wgt))

for i in range(len(lst)):
    sml=i
    for j in range(i,len(lst)):
        if lst[j][2]<lst[sml][2]:
            sml=j
    temp=lst[i]
    lst[i]=lst[sml]
    lst[sml]=temp

for i in range(len(lst)):
    st,des,w=lst[i]
    DSU(parent, st,des,w)

outfile.write(f"{count}")

inpfile.close()
outfile.close()