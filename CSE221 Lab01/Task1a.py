output_file=open('output1a.txt', 'w')

file_object= open('input1a.txt', 'r')

T=int(file_object.readline())

for i in range(T):
    num=int(file_object.readline())
    if num%2==0:
        res=f"\n{num} is an Even number"
        output_file.write(res)
    else:
        res=f"\n{num} is an Odd number"
        output_file.write(res)

inpfile.close()
outfile.close()