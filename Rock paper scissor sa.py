import random

lis = ["Rock", "Scissor", "Paper"]

'''
Rock vs Paper -> Paper wins
Rock vs Scissor -> Rock wins
Paper vs Scissor -> Scissor wins
'''

while True:

    usercount = 0
    Computercount = 0

    userchoice = int(input('''
Game Start.....
1. Yes
2. No | Exit
'''))

    if userchoice == 1:

        for g in range(1, 6):

            userInput = int(input('''
1.Rock
2.Scissor
3.Paper
'''))

            if userInput == 1:
                userchoice = "Rock"
            elif userInput == 2:
                userchoice = "Scissor"
            elif userInput == 3:
                userchoice = "Paper"
            else:
                print("Invalid Choice")
                continue

            Computerchoice = random.choice(lis)

            if Computerchoice == userchoice:
                print("Computer Value", Computerchoice)
                print("User Value", userchoice)
                print("Game Draw")

            elif (userchoice == "Rock" and Computerchoice == "Scissor") or \
                 (userchoice == "Paper" and Computerchoice == "Rock") or \
                 (userchoice == "Scissor" and Computerchoice == "Paper"):

                print("Computer Value", Computerchoice)
                print("User Value", userchoice)
                print("You Win")
                usercount = usercount + 1

            else:
                print("Computer Value", Computerchoice)
                print("User Value", userchoice)
                print("Computer Win")
                Computercount = Computercount + 1

        if usercount == Computercount:
            print("Final Game Draw....")
            print("User Score", usercount)
            print("Computer Score", Computercount)

        elif usercount > Computercount:
            print("Final You Win The Game...")
            print("User Score", usercount)
            print("Computer Score", Computercount)

        else:
            print("Final Computer Win The Game...")
            print("User Score", usercount)
            print("Computer Score", Computercount)

    else:
        break

