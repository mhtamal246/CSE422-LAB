
def divide(lst,final=0):
    if len(lst) <= 1:
        return lst,0

    mid = len(lst) // 2
    left,count1 = divide(lst[0:mid])
    right,count2 = divide(lst[mid:])

    conquered,curCount=conquer(left,right)

    if curCount>final:
        final=curCount

    return conquered, final

def conquer(left, right):
    count=0
    lis=[]
    lis.extend(left)
    lis.extend(right)

    cnt=0
    for i in lis:
        if i==0:
            cnt+=1
        else:
            if cnt>count:
                count=cnt
            cnt=0

    return lis,count

stg = "101000000011"
lst = [int(i) for i in stg]
res,count = divide(lst)
print(count)
