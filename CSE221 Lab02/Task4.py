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
        if lst[i][1]>lst[j][1]:
            sml=j
    temp=lst[i]
    lst[i]=lst[sml]
    lst[sml]=temp
print(lst)###########


menlst=[0]*M
count=1*len(menlst)
for i in range(len(menlst)):
    menlst[i]=lst[i]

print(menlst)###################

cnt=len(lst)
point=0
l=len(menlst)
while cnt>=0:
    for i in range(l+1,len(lst)):
        if point>=len(menlst)-1:
            point=0

        if menlst[point][1]<=lst[i][0]:
            menlst[0]=lst[i]
            point+=1
            count+=1
            l+=1

        if menlst[point][1]>=lst[i][0]:
            menlst[1]=lst[i]
            point+=1
            count+=1
            l+=1
    cnt-=1

print(count)##################
