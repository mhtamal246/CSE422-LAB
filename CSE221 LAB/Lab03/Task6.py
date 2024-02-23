inpfile = open("input6.txt", "r")
outfile = open("output6.txt", "w")

N = inpfile.readline()
N = int(N)

num = inpfile.readline()
num = num.split(" ")
lst = []
for i in num:
    lst.append(int(i))

def quicksort(lst, p1, p2):
    if p1<p2:
        part=partition(lst, p1, p2)
        quicksort(lst, p1, part-1)
        quicksort(lst, part+1, p2)
    return lst
def partition(lst, p1,p2):
    pivot=lst[p1]
    i=p1+1
    j=p2
    while True:
        while i<=j and lst[i]<=pivot:
            i+=1
        while i<=j and lst[j]>=pivot:
            j-=1
        if i<=j:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
        else:
            break
    tmp=lst[p1]
    lst[p1]=lst[j]
    lst[j]=tmp
    return j

srt=quicksort(lst, 0, len(lst)-1)
stg=""
for i in srt:
    stg+= str(i)+" "

outfile.write(f"{stg[:len(stg)-1]}")