outfile=open('output4.txt','w')
inpfile=open('input4.txt','r')


N=int(inpfile.readline())

name=[0]*N
location=[0]*N
hour=[0]*N
asci=[0]*N
time=[0]*N
for i in range(N):
    line= inpfile.readline()
    line=line.split(" ")

    for j in range(len(line)):
        if j==0:
            name[i]=line[j]
        if j==4:
            location[i]=line[j]
        if j==6:
            time[i] = line[j]

            ln=line[j].split(":")
            hour[i]=int(ln[0])

for i in range(len(name)):
    cal=0
    for j in name[i]:
        cal+=ord(j)
    asci[i]=cal

for i in range(len(name)):
    print(f"{name[i]}: {asci[i]}")
for i in range(len(asci)):
    sml=i
    for j in range(i, len(asci)):
        if asci[j]<asci[sml]:
            sml=j
        if asci[i]==asci[j]:
            if hour[i]<hour[j]:
                tm=hour[i]
                hour[i]=hour[j]
                hour[j]=tm

                tp=location[i]
                location[i]=location[j]
                location[j]=tp
    tmm=asci[i]
    asci[i]=asci[sml]
    asci[sml]=tmm

    temp=name[i]
    name[i]=name[sml]
    name[sml]=temp

    tmp=location[i]
    location[i]=location[sml]
    location[sml]=tmp

    tem=hour[i]
    hour[i]=hour[sml]
    hour[sml]=tem

    tpm=time[i]
    time[i]=time[sml]
    time[sml]=tpma

for i in range(len(asci)):
    outfile.write(f"{name[i]} will departure for {location[i]} at {time[i]}\n")


inpfile.close()
outfile.close()


