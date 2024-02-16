inpfile=open("input(1.2).txt", "r")
outfile=open("output(1.2)).txt", "w")

N= inpfile.readline()
S= inpfile.readline()
num,sum=N.split(" ")
S=S.split(" ")

elems=[]
sum=int(sum)
for i in S:
    elems.append(int(i))


one=0
two=len(elems)-1
idx1=None
idx2=None

while one<two:
    tot=elems[one]+elems[two]
    if tot==sum:
        idx1=one+1
        idx2=two+1
        break
    if tot<sum:
        one+=1
    if tot>sum:
        two-=1

if idx1 and idx2!=None:
    res= f"{idx1} {idx2}"
else:
    res=f"IMPOSSIBLE"
outfile.write(f"{res}")

inpfile.close()
outfile.close()