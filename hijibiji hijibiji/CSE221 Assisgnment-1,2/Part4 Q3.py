
def divide(stg,final=0):
    if len(stg) <= 1:
        return stg,0

    mid = len(stg) // 2
    left,count1 = divide(stg[0:mid])
    right,count2 = divide(stg[mid:])

    conquered,curCount=conquer(left,right)

    if curCount>final:
        final=curCount

    return conquered, final

def conquer(left, right):
    count=0

    L_cnt=0
    for i in left:
        if i=="0":
            L_cnt+=1
        else:
            if L_cnt>count:
                count=L_cnt
            L_cnt=0

    R_cnt=0
    for i in right:
        if i=="0":
            R_cnt+=1
        else:
            if R_cnt>count:
                count=R_cnt
            R_cnt=0

    cnt=0
    for i in range(len(left)-1,-1,-1):
        if left[i]=="0":
            cnt+=1
        else:
            break
    for j in right:
        if j=="0":
            cnt+=1
        else:
            break

    if cnt>count:
        count=cnt

    return left+right,count

stg = "10101010101010"
res,count = divide(stg)
print(count)
