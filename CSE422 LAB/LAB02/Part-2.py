inpfile=open("input.txt","r")
import random
cNumber=0
tSlot=0
courses=[]

counter=0
for i in inpfile:
    i=i.strip()
    if counter==0:
        line=i.split(" ")
        cNumber= int(line[0])
        tSlot= int(line[1])
        counter+=1
    else:
        courses.append(i)
        counter+=1

def population_maker_2(count):
    population=[]
    for i in range(count):
        lst=[]
        for j in range(cNumber*tSlot):
            rd=random.randint(0,1)
            lst.append(rd)
        population.append(lst)
    return population

def two_point_cross_2(p1,p2):
    point1=random.randint(1,len(p1)-2)
    point2=random.randint(point1+1,len(p2)-2)

    c1=p1[:point1]+p2[point1:point2]
    c2=p2[:point1]+p1[point1:point2]

    c1=c1+p1[point2:]
    c2=c2+p2[point2:]

    return c1,c2


def random_parent_2(population):
    p1=random.randint(0,len(population)-1)
    p2=random.randint(0,len(population)-1)

    return population[p1],population[p2]

def genALGO_2(size):
    size=size*2
    initial_population= population_maker(size)

    prnt1,prnt2=random_parent(initial_population)
    cld1,cld2=two_point_cross(prnt1,prnt2)

    return cld1,cld2

off1, off2= genALGO(int(input("Insert Population Size(int): ")))
print(f"Offspring 1: {off1}\nOffspring 2: {off2}")