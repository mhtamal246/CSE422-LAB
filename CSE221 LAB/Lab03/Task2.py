inpfile=open("input2.txt","r")
outfile=open("output2.txt","w")

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

    if a1>a2:
        max=a1
    else:
        max=a2
    return max

num=mergesort(lst)
outfile.write(f"{num[0]}")

####Time complexity of my code is O(nlogn)####