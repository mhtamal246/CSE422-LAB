arr=[1, 3, 4, 5, 9, 6, 2, -1]

def binary(arr,max=0):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=(left+right)//2
        max=arr[mid]
        if mid==left and mid==right:
            max=arr[mid]
            return max

        elif arr[mid-1]<max>arr[mid+1]:
            max=arr[mid]
            return max

        elif arr[mid+1]>max:
            left=mid+1

        elif arr[mid-1]>max:
            right=mid-1


res=binary(arr)
print(res)