arr= [23,2,19,3,7,11,5]
lst=[]
lst2=[]
for i in range(1,len(arr)-1,2):
    lst.append(arr[i])

for i in range(len(arr)-1,-1,-2):
    lst2.append(arr[i])

p1=0
p2=0
final=[]
while p1<len(lst) and p2<len(lst2):
    if lst[p1]<lst2[p2]:
        final.append(lst[p1])
        p1+=1
    else:
        final.append(lst2[p2])
        p2+=1

if p1<len(lst):
    for i in range(p1,len(lst)):
        final.append(lst[i])

if p2<len(lst2):
    for i in range(p2,len(lst2)):
        final.append(lst2[i])

print(final)