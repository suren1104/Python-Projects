import random

choise = "RPS"


def user_pick():
    print("CHOISES:\n (R)ROCK\n (P)PAPER\n (S)SISSOR")
    print("PICK ANYONE FROM THE CHOISE:")
    global pick
    pick = input()


def computer_pick():
    c_p = random.randint(0, 2)
    global computer_pick
    computer_pick = choise[c_p]


def result():
    print("YOUR PICK:", pick)
    print("COMPUTER PICK:", computer_pick)
    if pick == computer_pick:
        print("You and Computer pick same one ----- DRAW!!")
    elif pick == "R" and computer_pick == "S":
        print("YOU WIN!!")
    elif pick == "S" and computer_pick == "P":
        print("YOU WIN!!")
    elif pick == "P" and computer_pick == "R":
        print("YOU WIN!!")

    elif pick == "R" and computer_pick == "P":
        print("YOU LOSE!!")
    elif pick == "P" and computer_pick == "S":
        print("YOU LOSE!!")
    elif pick == "S" and computer_pick == "R":
        print("YOU LOSE!!")
    else:
        print("Check YOUR PICK!!")


print("IF YOU WANT TO PLAY THIS ROCK PAPER AND SISSOR GAME:")
ans2 = input().lower()
if ans2 == "yes":
    user_pick()
    computer_pick()
    result()
else:
    print("THANK YOU!!")
