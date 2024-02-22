inpfile = open("input3.txt", "r")
outfile = open("output3.txt", "w")

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
    a1, inv1 = mergesort(lst[:mid])
    a2, inv2 = mergesort(lst[mid:])
    merged, inv = merge(a1, a2)
    return merged, inv + inv1 + inv2

def merge(a1, a2, inv_count = 0):
    i = 0
    j = 0
    sorted_lst = []
    while (i < len(a1) and j < len(a2)):
        if a1[i] <= a2[j]:
            sorted_lst.append(a1[i])
            i += 1
        else:
            sorted_lst.append(a2[j])
            j += 1
            inv_count += len(a1) - i
    sorted_lst.extend(a1[i:])
    sorted_lst.extend(a2[j:])
    return sorted_lst, inv_count

merged, inversion_count = mergesort(lst)

outfile.write(f"{inversion_count}")
inpfile.close()
outfile.close()
