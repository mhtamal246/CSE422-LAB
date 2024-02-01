outfile=open('output1b.txt','w')

inpfile=open('input1b.txt','r')

T=int(inpfile.readline())

for i in range(T):
    lst=inpfile.readline()
    lst=lst.split()
    num1=int(lst[1])
    sign=lst[2]
    num2=int(lst[3])
    if sign=="+":
        res=num1+num2
    elif sign=="-":
        res=num1-num2
    elif sign=="*":
        res=num1*num2
    elif sign=="/":
        res=num1/num2
    result=f"The result of {num1} {sign} {num2} is {res}\n"
    outfile.write(result)

inpfile.close()
outfile.close()