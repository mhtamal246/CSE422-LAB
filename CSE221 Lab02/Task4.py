inpfile=open("input4.txt","r")
outfile=open("output4.txt","w")
inp=inpfile.readline()

N,M=inp.split()
N=int(N)
M=int(M)
lst=[]

for i in range(N):
    S=inpfile.readline()
    a,b=S.split(" ")
    lst.append((int(a),int(b)))

for i in range(len(lst)):
    sml=i
    for j in range(i+1,len(lst)):
        if lst[j][1]<lst[sml][1]:
            sml=j
    lst[i],lst[sml]=lst[sml],lst[i]

menlst=[0]*M
accept=[0]*M
count=0
idx=0
for work in range(len(lst)):
    start=lst[work][0]
    end=lst[work][1]
    for j in range(len(menlst)):
        accept[j]=start-menlst[j]

    c= float("inf")
    for k in range(len(accept)):
        if accept[k]<c and accept[k]>=0:
            c=accept[k]
            idx=k
    if menlst[idx]<=start and c>=0:
        menlst[idx]=end
        count+=1
    idx=0

outfile.write(f"{count}")
