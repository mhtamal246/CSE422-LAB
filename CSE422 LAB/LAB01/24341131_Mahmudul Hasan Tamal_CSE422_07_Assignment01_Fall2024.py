inpfile=open("input.txt","r")

flag=False
dict_for_hueristic={}
dict_for_cost={}
#Dictionary for the cost and hueristic:
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


#A* search-Algorithm Start:
import heapq
path=[]
visited=[]

def Astar_Search(source, goal):
    global path, visited, dict_for_cost, dict_for_hueristic
    queue = []
    parent = {source: None}
    cost = {source: 0}
    queue.append((dict_for_hueristic[source]+0, source))


    while queue:
        heapq.heapify(queue)
        cst, loc = queue.pop(0)

        if loc == goal:
            path = []
            stg = ""
            while loc:                  #back track can be done from the goal to source. in every iteration we check where this node came from
                path.append(loc)
                loc = parent[loc]
            path.reverse()
            for i in path:
                stg += i + " -> "
            return f"Path: {stg.strip(' -> ')}\nTotal Distance: {cost[goal]} km"

        for i in dict_for_cost[loc]:
            neighbor = i[0]
            actual_cost = i[1]
            new_cost = cost[loc] + actual_cost

            if neighbor not in cost:
                cost[neighbor] = new_cost
                queue.append((dict_for_hueristic[neighbor]+ new_cost, neighbor))
                parent[neighbor] = loc

            elif new_cost < cost[neighbor]:                      #new cost must be less than previous one
                cost[neighbor] = new_cost
                parent[neighbor] = loc
                queue.append((dict_for_hueristic[neighbor]+ new_cost, neighbor))
    return "NO PATH FOUND"



print(Astar_Search(str(input("Starting Node in First letter Capital: ")), str(input("Goal Node in First letter Capital: "))))                #Name first letter in Capital

