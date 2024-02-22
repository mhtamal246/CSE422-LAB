inpfile = open("input5.txt", "r")
outfile = open("output5.txt", "w")

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
    pivot=lst[p2]
    i=p1-1
    for j in range(p1,p2):
        if lst[j]<=pivot:
            i=i+1
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp

    tmp=lst[i+1]
    lst[i+1]=lst[p2]
    lst[p2]=tmp
    return i+1

srt=quicksort(lst, 0, len(lst)-1)
stg=""
for i in srt:
    stg+= str(i)+" "

outfile.write(f"{stg[:len(stg)-1]}")