inpfile=open("input(1.1).txt", "r")
outfile=open("output(1.1).txt", "w")

N= inpfile.readline()
S= inpfile.readline()
num,sum=N.split(" ")
S=S.split(" ")

elems=[]
sum=int(sum)
for i in S:
    elems.append(int(i))
idx1=None
idx2=None
flag=False

for i in range(len(elems)):
    for j in range(i+1,len(elems)):
        if elems[i]+elems[j]==sum:
            idx1=i+1
            idx2=j+1
            flag=True
            break
    if flag:
        break

if idx1 and idx2!=None:
    res= f"{idx1} {idx2}"
else:
    res=f"IMPOSSIBLE"

outfile.write(f"{res}")

inpfile.close()
outfile.close()