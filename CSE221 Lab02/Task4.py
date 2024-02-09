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
print(lst)
menlst=[0]*M
count=0

for work in lst:
    start=work[0]
    end=work[1]
    for i in range(len(menlst)):
        if menlst[i]<=start:
            menlst[i]=end
            count+=1
            break
print(count)
