inpfile = open("input6.txt", "r")
outfile = open("output6.txt", "w")

N = inpfile.readline()
N = int(N)

num = inpfile.readline()
num = num.split(" ")
lst = []
for i in num:
    lst.append(int(i))

Q=inpfile.readline()
Q=int(Q)

for i in range(Q):
    nm=inpfile.readline()
    nm=int(np)

