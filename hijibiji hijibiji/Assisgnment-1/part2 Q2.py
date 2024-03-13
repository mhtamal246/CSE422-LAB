

def binary(arr,fnd,count=0):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==fnd:
            count+=1
            for i in range(mid-1,0,-1):
                if arr[i]==fnd:
                    count+=1
                else:
                    break
            for i in range(mid+1,len(arr)-1):
                if arr[i]==fnd:
                    count+=1
                else:
                    break
            return count
        elif arr[mid]<fnd:
            left=mid-1
        elif arr[mid>fnd]:
            right=mid+1
    return count



arr = [1, 3, 4, 5, 13, 15,16,16, 16, 16, 16, 16,16,16, 19, 21, 21, 23]
res=binary(arr,16)

print(res)