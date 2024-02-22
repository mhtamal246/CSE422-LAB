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
        return lst, 0  # Return the sorted list and inversion count
    mid = len(lst) // 2
    a1, inv1 = mergesort(lst[:mid])
    a2, inv2 = mergesort(lst[mid:])
    merged, inv = merge(a1, a2)
    return merged, inv + inv1 + inv2  # Total inversion count

def merge(a1, a2):
    i = 0
    j = 0
    sorted_lst = []
    max_sum = 0  # Maximum sum of squared pairs
    while (i < len(a1) and j < len(a2)):
        if a1[i] + a2[j] ** 2 > max_sum:
            max_sum = a1[i] + a2[j] ** 2
        if a1[i] < a2[j]:
            sorted_lst.append(a1[i])
            i += 1
        else:
            sorted_lst.append(a2[j])
            j += 1

    sorted_lst.extend(a1[i:])
    sorted_lst.extend(a2[j:])

    return sorted_lst, max_sum

merged, max_sum = mergesort(lst)
stg = " ".join(map(str, merged))
outfile.write(stg)

print("Maximum value of A[i] + A[j]^2:", max_sum)

inpfile.close()
outfile.close()
