outfile=open('output4.txt','w')
inpfile=open('input4.txt','r')
N=int(inpfile.readline())

lst=[]

for i in range(N):
    line=inpfile.readline()
    line=line.split(" ")
    lst.append(line)

for i in range(len(lst)):
    sml=i
    for j in range(i,len(lst)):
        if lst[j][0]<lst[sml][0]:
            sml=j

        if lst[i][0]==lst[j][0]:
            spt=lst[i][6].split(":")
            if lst[i][6][int(0)]>lst[j][6][int(0)]:

                tmp=lst[j]
                lst[j]=lst[i]
                lst[i]=tmp
    temp=lst[i]
    lst[i]=lst[sml]
    lst[sml]=temp

for i in range(len(lst)):
    outfile.write(f"{lst[i][0]} will departure for {lst[i][4]} at {lst[i][6]}")

