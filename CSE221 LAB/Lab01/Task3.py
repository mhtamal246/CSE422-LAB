outfile=open('output3.txt', 'w')
inpfile=open('input3.txt', 'r')

N=int(inpfile.readline())
st=inpfile.readline()
mk=inpfile.readline()
std=st.split(" ")
mrk=mk.split(" ")
lst=[0]*N
count=0

for i in range(len(std)):
    lst[i]= (int(std[i]),int(mrk[i]))
print(lst)

for i in range(len(lst)):
    lrg=i
    for j in range(i, len(lst)):
        if lst[j][1]>lst[lrg][1]:
            lrg=j
        if lst[j][1]==lst[lrg][1]:
            if lst[lrg][0]>lst[j][0]:
                tmp=lst[j]
                lst[j]=lst[lrg]
                lst[lrg]=tmp

    temp=lst[i]
    lst[i]=lst[lrg]
    lst[lrg]=temp
print(lst)

for i in range(len(lst)):
    outfile.write(f"ID: {lst[i][0]} Mark: {lst[i][1]}\n")

inpfile.close()
outfile.close()