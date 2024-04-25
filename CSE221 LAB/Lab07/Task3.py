inpfile= open("input3.txt","r")
outfile= open("output3.txt","w")

N=inpfile.readline()
N=int(N)


def climbing(N,DP=[0]*(N+1)):
    if DP[N]!=0:
        return DP[N]
    if N<=1 or N<=2:
        return N

    res= climbing(N-1)+climbing(N-2)
    DP[N]=res
    return res

outfile.write(f"{climbing(N)}")
inpfile.close()
outfile.close()