import numpy as np
outfile=open('output3.txt','w')
inpfile=open('input3.txt','r')

N=int(inpfile.readline())
st=inpfile.readline()
mk=inpfile.readline()
st=st.split(" ")
mk=mk.split(" ")

std=np.array([0]*N)
mrk=np.array([0]*N)
for i in range(len(st)):
    std[i]=int(st[i])
for i in range(len(mk)):
    mrk[i]=int(mk[i])

for i in range(len(std)-1):
    for j in range(len(mrk)-1-i):
        if mrk[j]<mrk[j+1]:
            temp=mrk[j+1]
            tmp=std[j+1]
            mrk[j+1]=mrk[j]
            std[j+1]=std[j]
            mrk[j]=temp
            std[j]=tmp

for i in range(len(std)):
    outfile.write(f"ID: {std[i]} Mark: {mrk[i]}\n")

inpfile.close()
outfile.close()