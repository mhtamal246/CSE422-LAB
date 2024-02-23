inpfile = open("input4.txt", "r")
outfile = open("output4.txt", "w")

N = inpfile.readline()
N = int(N)

num = inpfile.readline()
num = num.split(" ")
lst = []
for i in num:
    lst.append(int(i))

def mergesort(lst):
    if len(lst) <= 1:
        return lst, 0
    mid = len(lst) // 2
    a1, max_sum1 = mergesort(lst[:mid])
    a2, max_sum2 = mergesort(lst[mid:])
    finalmax = max_sum1
    if max_sum2 > finalmax:
        finalmax = max_sum2

    merged, cur_max = merge(a1, a2)
    if cur_max > finalmax:
        finalmax = cur_max
    return merged, finalmax
def merge(a1, a2):
    comb = []
    max_sum = 0

    maxnum=float("-inf")
    maxsq=float("-inf")
    for i in a1:
        if i>maxnum:
            maxnum=i
    for j in a2:
        if j**2>maxsq:
            maxsq=j**2
    if maxnum+maxsq>max_sum:
        max_sum= maxnum+maxsq

    comb.extend(a1[0:len(a1)])
    comb.extend(a2[0:len(a2)])

    nm = float("-inf")
    sq = float("-inf")
    idx=""
    for x in range(len(comb)):
        if comb[x]>nm:
            nm=comb[x]
            idx=x
    for y in range(idx+1,len(comb)):
        if comb[y]**2>sq:
            sq=comb[y]**2

    if nm+sq>max_sum:
        max_sum= nm+sq
    return comb, max_sum

merged, max_sum = mergesort(lst)
outfile.write(f"{max_sum}")

inpfile.close()
outfile.close()
