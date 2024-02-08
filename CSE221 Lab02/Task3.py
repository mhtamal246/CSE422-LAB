inpfile=open("input3.txt","r")
outfile=open("output3.txt","w")

N=inpfile.readline()
N=int(N)
lst=[]

for i in range(N):
    S=inpfile.readline()
    a,b=S.split(" ")
    lst.append((int(a),int(b)))
print(lst)
for i in range(len(lst)):
    sml=i
    for j in range(len(lst)):
        if lst[i][1]>lst[j][1]:
            sml=j

    temp=lst[i]
    lst[i]=lst[sml]
    lst[sml]=temp
print(lst)

idx=0
count=0
mainlst=[]
for i in range(idx,len(lst)):
    for j in range(i+1,len(lst)):

            pass