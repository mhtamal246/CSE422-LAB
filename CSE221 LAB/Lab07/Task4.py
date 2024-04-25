inpfile= open("input4.txt","r")
outfile= open("output4.txt","w")

count, target_sum=inpfile.readline().split(" ")
count,target_sum=int(count),int(target_sum)

coins=inpfile.readline().split(" ")

for i in range(len(coins)):
    coins[i]=int(coins[i])

dp=[float("inf")]* (target_sum+1)

for target in range(1,len(dp)):
    count=0
    for coin in coins:
        if coin>target:
            continue
        if coin==target:
            dp[target]=1
        if target>coin:
            remain=target-coin
            if 1+dp[remain]<dp[target]:
                dp[target]=1+dp[remain]

outfile.write(f"{dp[len(dp)-1]}")

inpfile.readline()
outfile.readline()


