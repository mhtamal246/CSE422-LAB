inpfile=open("input(2.1).txt", "r")
outfile=open("output(2.1)).txt", "w")

n1=inpfile.readline()
l1=inpfile.readline()
n2=inpfile.readline()
l2=inpfile.readline()
n1=int(n1)
n2=int(n2)
l1=l1.split(" ")
l2=l2.split(" ")
lst1=[]
lst2=[]
for i in l1:
    lst1.append(int(i))
for i in l2:
    lst2.append(int(i))

lst1.extend(lst2)
lst1.sort()

res=""
for i in lst1:
    res+=str(i)+" "
res= res[:len(res)-1]

outfile.write(f"{res}")

inpfile.close()
outfile.close()