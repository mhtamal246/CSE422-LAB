inpfile = open("input6.txt", "r")
outfile = open("output6.txt", "w")

N = inpfile.readline()
N = N.split(" ")
N=int(N[0])

num = inpfile.readline()
num = num.split(" ")
lst = []
for i in num:
    lst.append(int(i))

def quicksort(lst, p1, p2,k):
    if p1 == p2:
        return lst[p1]
    part = partition(lst, p1, p2)

    if k == part:
        return lst[k]
    elif k<part:
        return quicksort(lst, p1, part - 1, k)
    else:
        return quicksort(lst, part + 1, p2, k)
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
            lst[i], lst[j] = lst[j], lst[i]
        else:
            break
    lst[p1], lst[j] = lst[j], lst[p1]
    return j

que=inpfile.readline()
que=que.split(" ")
que=int(que[0])

for i in range(que):
    k=inpfile.readline()
    k=int(k)
    srt=quicksort(lst, 0, len(lst)-1,k-1)
    outfile.write(f"{srt}\n")