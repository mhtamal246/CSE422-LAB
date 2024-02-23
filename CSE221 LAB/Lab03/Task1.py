inpfile=open("input1.txt","r")
outfile=open("output1.txt","w")

N=inpfile.readline()
N=int(N)

num= inpfile.readline()
num=num.split(" ")
lst=[]
for i in num:
    lst.append(int(i))

def mergesort(lst):
    if len(lst)<=1:
        return lst
    mid=len(lst)//2
    a1=mergesort(lst[:mid])
    a2=mergesort(lst[mid:])
    return merge(a1, a2)

def merge(a1,a2):
    i=0
    j=0
    sorted=[]
    while(i<len(a1) and j<len(a2)):
        if a1[i]<a2[j]:
            sorted.append(a1[i])
            i+=1
        else:
            sorted.append(a2[j])
            j+=1

    sorted.extend(a1[i:len(a1)])
    sorted.extend(a2[j:len(a2)])
    return sorted
merged=mergesort(lst)
stg=""
for i in merged:
    stg+=str(i)+" "

outfile.write(f"{stg[:len(stg)-1]}")

inpfile.close()
outfile.close()