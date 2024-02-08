inpfile=open("input3.txt","r")
outfile=open("output3.txt","w")

N=inpfile.readline()
N=int(N)
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

count=1
mainlst=[]
mainlst.append(lst[0])

c=len(lst)
i=0
while c>=0:
    for j in range(len(lst)):
        if lst[i][1]<=lst[j][0]:
            mainlst.append(lst[j])
            i=lst[j]
            count+=1
            i=j
            break
    c-=1

#for i in range(len(lst)):
#    for j in range(i+1,len(lst)):
#       if lst[i]!=0 and lst[j]!=0:
#            if lst[i][1]<=lst[j][0]:
#                mainlst.append(lst[j])
#                count+=1
#                break
#            else:
#               lst[j]=0

outfile.write(f"{count}\n")
for i in range(len(mainlst)):
    outfile.write(f"{mainlst[i][0]} {mainlst[i][1]}\n")
