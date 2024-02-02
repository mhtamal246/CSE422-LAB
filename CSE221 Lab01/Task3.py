outfile=open('output3.txt', 'w')
inpfile=open('input3.txt', 'r')

N=int(inpfile.readline())
st=inpfile.readline()
mk=inpfile.readline()
std=st.split(" ")
mrk=mk.split(" ")

for i in range(len(std)):
    std[i]=int(std[i])
for i in range(len(mrk)):
    mrk[i]=int(mrk[i])

for i in range(len(std)):
    lrg=i
    for j in range(i,len(mrk)):
        if mrk[j]>mrk[lrg]:
            lrg=j
        if mrk[i]==mrk[j]:
            if std[i]>std[j]:
                tp=std[i]
                std[i]=std[j]
                std[j]=tp
    temp=mrk[i]
    mrk[i]=mrk[lrg]
    mrk[lrg]=temp

    tmp=std[i]
    std[i]=std[lrg]
    std[lrg]=tmp

for i in range(len(std)):
    outfile.write(f"ID: {std[i]} Mark: {mrk[i]}\n")

inpfile.close()
outfile.close()