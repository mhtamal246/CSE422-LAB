inpfile= open("input3.txt","r")
outfile= open("output3.txt","w")

N=inpfile.readline()
N=int(N)


def climbing(N,lst=[0]*(N+1)):
    if lst[N]!=0:
        return lst[N]
    if N<=1 or N<=2:
        return N

    res= climbing(N-1)+climbing(N-2)
    lst[N]=res
    return res

outfile.write(f"{climbing(N)}")
inpfile.close()
outfile.close()