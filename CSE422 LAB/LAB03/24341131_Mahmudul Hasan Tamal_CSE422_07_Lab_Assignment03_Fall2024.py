
########################################################## PART-1 ######################################################
import random
def kombat(starts, depth=0, branch=2, maximizer= True, alpha=float("-inf"), beta=float("inf")):
    if depth==5:
        rd= random.choice([1, -1])
        return rd

    if maximizer:
        for i in range(branch):
            res= kombat(starts, depth+1, branch, False, alpha, beta)
            if res>alpha:
                alpha= res
            if alpha>=beta:
                break
            else:
                continue
        return alpha

    if not maximizer:
        for i in range(branch):
            res= kombat(starts, depth+1, branch, True, alpha, beta)
            if res<beta:
                beta=res
            if alpha>=beta:
                break
            else:
                continue
        return beta


def FightRounds(starts, rounds, Scorpion=0, Sub_Zero=0, winners=[] ):
    if starts!=0 and starts!=1:
        return "Invalid Input", "Invalid Input", "Invalid Input"
    for i in range(rounds):
        if starts==0:
            if i%2==0:
                win= kombat(starts)
                if win==1:
                    Scorpion+=1
                    winners.append("Scorpion")
                else:
                    Sub_Zero+=1
                    winners.append("Sub_Zero")

            else:
                win= kombat(1)
                if win==1:
                    Sub_Zero+=1
                    winners.append("Sub_Zero")
                else:
                    Scorpion+=1
                    winners.append("Scorpion")

        if starts==1:
            if i%2==0:
                win= kombat(starts)
                if win==1:
                    Sub_Zero+=1
                    winners.append("Sub_Zero")
                else:
                    Scorpion+=1
                    winners.append("Scorpion")

            else:
                win= kombat(0)
                if win==1:
                    Scorpion+=1
                    winners.append("Scorpion")
                else:
                    Sub_Zero+=1
                    winners.append("Sub_Zero")


    return Scorpion, Sub_Zero, winners


sc, sub, winners= FightRounds(int(input("Enter starting player (0 for Scorpion, 1 for Sub-Zero): ")), 3)

if sc=="Invalid Input" and sub=="Invalid Input" and winners=="Invalid Input":
    print("Invalid Input")
else:
    if sc>sub:
        print("\nGame Winner: Scorpion")
    if sc<sub:
        print("Game Winner: Sub-Zero")
    print("Total Rounds Played: 3\n")
    for i in range(len(winners)):
        print(f"Winner of Round {i+1}: {winners[i]}")
########################################################## END OF PART-1 ###############################################



########################################################## PART-2 ######################################################
def without_magic(c, values, depth=0, branch=2, maximizer= True, alpha=float("-inf"), beta=float("inf")):
    global index
    if depth==3:
        ind=values[index]
        index+=1
        return ind

    if maximizer:
        for i in range(branch):
            res= without_magic(c, values, depth+1, branch, False, alpha, beta)
            if res>alpha:
                alpha= res
            if alpha>=beta:
                break
            else:
                continue
        return alpha

    if not maximizer:
        for i in range(branch):
            res= without_magic(c, values, depth+1, branch, True, alpha, beta)
            if res<beta:
                beta=res
            if alpha>=beta:
                break
            else:
                continue
        return beta

def with_magic(c, values, left_tree=[], right_tree=[]):
    global index
    for i in range(len(values)):
        if i<= (len(values)//2)-1:
            left_tree.append(values[i])
        else:
            right_tree.append(values[i])

    L_val=float("-inf")
    R_val=float("-inf")
    for i in left_tree:
        if L_val<i:
            L_val=i
    for i in right_tree:
        if R_val<i:
            R_val=i

    L_val=L_val-c
    R_val=R_val-c
    if L_val>R_val:
        return L_val, "left"
    else:
        return R_val, "right"

def pacman_game(c):
    global index
    given_values=[3, 6, 2, 3,    7, 1, 2, 0]

    magic_val, direction= with_magic(c, given_values)
    prun_val=without_magic(c, given_values)

    if magic_val>prun_val:
        print(f"The minimax value is {magic_val}. Pacman goes {direction} and uses dark magic")
    elif magic_val==prun_val:
        print("The minimax value is the same. Both are equally beneficial for Pacman")
    else:
        print(f"The minimax value is {prun_val}. Pacman does not use dark magic")


index = 0
pacman_game(int(input("Enter an Integer: ")))

########################################################### END OF PART-2 ##############################################