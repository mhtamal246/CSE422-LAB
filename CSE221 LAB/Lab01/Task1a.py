
inpfile=open('input1a.txt','r')
outfile=open('output1a.txt','w')

T=int(inpfile.readline())


for i in range(T):
    line=int(inpfile.readline())
    if line%2==0:
        outfile.write(f"{line} is a even number\n")
    else:
        outfile.write(f"{line} is a odd number\n")

inpfile.close()
outfile.close()