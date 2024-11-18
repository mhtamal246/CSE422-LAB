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

def population_maker(count):
    population=[]
    for i in range(count):
        lst=[]
        for j in range(cNumber*tSlot):
            rd=random.randint(0,1)
            lst.append(rd)
        population.append(lst)
    return population

def fitness(chromlist):
    overlap=0
    consistency=0

    for i in range(0,len(chromlist),3):
        count = 0
        for j in range(i,i+3):
            if chromlist[j]==1:
                count+=1
        overlap+=abs(count-1)

    c = 0
    for i in range(tSlot):
        cnt=0
        for j in range(c,len(chromlist),3):
            if chromlist[j]==1:
                cnt+=1
        consistency+=abs(cnt-1)
        c+=1

    total_penalty= -abs(overlap+consistency)
    return total_penalty

def singlecross(p1,p2):
    num=random.randint(1,len(p1)-2)
    c1=p1[:num]+p2[num:]
    c2=p2[:num]+p1[num:]
    return c1,c2

def mutation(c1,c2):
    num=random.randint(0,len(c1)-1)
    if c1[num]==0:
        c1[num]=1
    if c1[num]==1:
        c1[num]=0
    num1 = random.randint(0, len(c2) - 1)
    if c2[num1]==0:
        c2[num1]=1
    if c2[num1]==1:
        c2[num1]=0
    return c1,c2

def random_parent(population):
    p1=random.randint(0,len(population)-1)
    p2=random.randint(0,len(population)-1)

    return population[p1],population[p2]

def genALGO(size, iteration, pFitness= float("-inf"), solution=[] ):
    size=size*2
    initial_population= population_maker(size)
    newlist=[]
    for i in range(iteration):
        for j in range(size):
            prnt1,prnt2=random_parent(initial_population)
            cld1,cld2=singlecross(prnt1,prnt2)
            cld1,cld2=mutation(cld1,cld2)
            newlist.append(cld1)
            newlist.append(cld1)

        initial_population=newlist
        for k in range(len(initial_population)):
            fit=fitness(initial_population[k])
        if pFitness<fit:
            pFitness=fit
            solution=initial_population[k]
        if fit==0:
            pFitness=fit
            solution=initial_population[k]
            break
        newlist = []
    return pFitness,solution

fitness, chromo= genALGO(int(input("Insert Population Size(int): ")), int(input("Insert Generation Size(int): ")))
print(f"{chromo}\n{fitness}")
