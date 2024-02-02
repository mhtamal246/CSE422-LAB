outfile=open('output4.txt','w')
inpfile=open('input4.txt','r')


N=int(inpfile.readline())

name=[0]*N
location=[0]*N
hour=[0]*N
asci=[0]*N
for i in range(N):
    line= inpfile.readline()
    line=line.split(" ")

    for j in range(len(line)):
        if j==0:
            name[i]=line[j]
        if j==4:
            location[i]=line[j]
        if j==6:
            ln=line[j].split(":")
            hour[i]=int(ln[0])
for i in range(len(name)):
    cal=0
    for j in name[i]:
        cal+=ord(j)
    asci[i]=cal


for i in range(len(asci)):
    sml=i
    for j in range(len(asci)):
        if asci[j+1]<asci[sml]:
            sml=j
        if asci[j]==asci[j+1]:
            if hour[j]<hour[j+1]:
                tm=



