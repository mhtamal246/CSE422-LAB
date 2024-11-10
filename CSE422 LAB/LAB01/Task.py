inpfile=open("input.txt","r")
outfile=open("output.txt","w")

flag=False
dict_for_hueristic={}
dict_for_cost={}

#This portion is to make the dictionary for the cost and hueristic
while True:
    if flag:
        break
    line=inpfile.readline().strip().split(" ")
    if line[0]=="Bucharest":
        flag=True

    dict_for_hueristic[line[0]]=int(line[1])

    for i in range(2,len(line),2):
        if line[0] not in dict_for_cost:
            dict_for_cost[line[0]]= [ (line[i],int(line[i+1])) ]
        else:
            dict_for_cost[line[0]].append( (line[i],int(line[i+1])) )

#This portion is for A* search Algorithm


