inpfile=open("input3.txt","r")
outfile=open("output3.txt","w")

N=inpfile.readline()
N=int(N)
lst=[]

for i in range(N):
    S=inpfile.readline()
    a,b=S.split(" ")
    lst.append((int(a),int(b)))

for i in

idx=0
count=0
mainlst=[]
for i in range(idx,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]