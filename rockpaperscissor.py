import random
computer=random.randint(0,2)
user=eval(input("Enter a no. b/w 0 and 2"))
assert user<3

if user==0:
    userHand = "Paper"
elif user==1:
    userHand = "Scissor"
else:
    userHand = "Rock"

if computer == 0:
    computerHand= "Paper"
elif computer==1:
    computerHand="Scissor"
else:
    computerHand="Rock"

if user==(computer+1)%3:
    print("The computer is",computerHand,"and the user is",userHand,".You won!")
elif user==(computer-1)%3:
    print("The computer is",computerHand,"and the user is",userHand,".The computer won!")
else:
    print("The computer is",computerHand,"and the user is",userHand,".it is a draw.")



