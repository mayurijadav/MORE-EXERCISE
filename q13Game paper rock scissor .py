# Yeh rock paper scissors game ka program hai. Iss game ko aap computer ke against kheloge. Iss game ke 3 rules hai

# Rock Paper se haar jata hai

# Paper Scissors se haar jaata hai

# Aur, Scissors Rock se.

# Appko pehle rock,paper ya scissors mei se chose karna hoga. Aur uske baad computer randomly inme se ek option chose karega. Firr, upar diye gaye rules ke hisab se result aayega. Jaise:

# Agar aapne "Rock" chose kiya aur computer ne "Scissors"

# To aap jeet jaoge kyunki "Rock" "Scissors" ko hara deta hai. ( Rule 3 )
import random
cchoice=["Rock","Paper","Scissor"]
while True:
    print("Rock paper scissor game")
    youwin,computerwin=0,0
    for i in range(1,6):
        print("Rock Paper Scissor Game")
        print("Please select any one option")
        print("1.Rock","2.Paper","3.Scissor",sep="\n")
        yourchoice=int(input())
    if yourchoice==1:
        print("you select Rock")
        yourchoice="Rock"
    elif yourchoice==2:
        print("your selected Paper")
        yourchoice="Paper"
    elif yourchoice==3:
        print("your selected Scissor")
        yourchoice="Scissor"
    else:
        print("Invallid choice")
        break
    computerchoice=random.choice(cchoice)
    print("computer select:",computerchoice)
    if yourchoice==computerchoice:
        youwin+=1
        computerwin+=1
        print("this round is draw")
    elif (yourchoice=="Paper" and yourchoice=="Rock") or (yourchoice=="Scissor"):
        youwin+=1
        print("you win this round")
    else:
        computerwin+=1
        print("computer win this round")
    if youwin>computerwin:
        print("you win the game")
        print("your score is:","your score ",youwin, "computer score:",computerwin,sep="")
    elif computerwin>youwin:
        print("you lose the game. computer win this game")
        print("score is :","your score:",youwin, "computer score:",computerwin,sep="")
    else:
        print("match drawn")
        print("score is :","your score:",youwin, "computer score:",computerwin,sep="")
    userchoice=input("want to play again? (yes/exit)")
    if userchoice=="yes" or userchoice=="yes" or userchoice=="yes":
        continue
    else:
        break
    # while reaning the game select the number from 1,2,3.
