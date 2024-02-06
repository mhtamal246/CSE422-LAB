inpfile=open("input(2.2).txt","r")
outfile=open("output(2.2)).txt","w")

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
while True:

    if one >= len(lst1) - 1 and two >= len(lst2) - 1:
        break

    elif one>=len(lst1)-1:
        mainlst.extend(lst2[two:])
        break
    elif two>=len(lst2)-1:
        mainlst.extend(lst1[one:])
        break

    else:
        if lst1[one]<lst2[two]:
            mainlst.append(lst1[one])
            one+=1
        if lst1[one]>lst2[two]:
            mainlst.append(lst2[two])
            two+=1

outfile.write(f"{mainlst}")

inpfile.close()
outfile.close()
