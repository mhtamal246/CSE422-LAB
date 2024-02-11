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
differ=[0]*M
count=0
idx=0
for work in range(len(lst)):
    start=lst[work][0]
    end=lst[work][1]
    for j in range(len(menlst)):
        differ[j]=start-menlst[j]

    time=float("inf")
    for k in range(len(differ)):
        if differ[k]<time and differ[k]>=0:
            time=differ[k]
            idx=k
    if menlst[idx]<=start and time>=0:
        menlst[idx]=end
        count+=1
    idx=0

outfile.write(f"{count}")

inpfile.close()
outfile.close()