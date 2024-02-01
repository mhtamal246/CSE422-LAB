import numpy as np
outfile = open('output2.txt', 'w')
inpfile = open('input2.txt', 'r')
T = int(inpfile.readline())
arr=np.array([0]*T)
num=inpfile.readline()
num=num.split(" ")
for i in range(len(num)):
    arr[i] = int(num[i])
def bubbleSort(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag=True
        if flag==False:
            return arr
    return arr
ar=bubbleSort(arr)
outfile.write(f"{ar}")
inpfile.close()
outfile.close()