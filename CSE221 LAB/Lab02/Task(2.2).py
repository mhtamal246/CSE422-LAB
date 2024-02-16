inpfile=open("input(2.2).txt", "r")
outfile=open("output(2.2)).txt", "w")

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
one=0
two=0
mainlst=[]
flag=False
while one <= len(lst1) and two <= len(lst2):

    if one>=len(lst1):
        mainlst.extend(lst2[two:])
        flag=True
    elif two>=len(lst2):
        mainlst.extend(lst1[one:])
        flag=True

    else:
        if lst1[one]<lst2[two]:
            mainlst.append(lst1[one])
            one+=1
        elif lst1[one]==lst2[two]:
            mainlst.append(lst1[one])
            one+=1
        elif lst1[one]>lst2[two]:
            mainlst.append(lst2[two])
            two+=1

    if flag:
        break
res=""
for i in mainlst:
    res+=str(i)+" "
res= res[:len(res)-1]

outfile.write(f"{res}")

inpfile.close()
outfile.close()

# For sample input-2: at 4th line of the output there's a space
#at the end so code gives error. please remove the space while checking.