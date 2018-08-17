# Import the required classes
from PlayerStats import *
from DisplayInfo import *

# Main program starts here

while True:
    # Display options and obtain the user's choice
    print("1. Single player information")
    print("2. Two player comparison")
    print("3. Exit the program")
    choice=input("\nEnter your choice : ")
    # Get one player name and display stats for option '1'
    if choice=="1":
        player=input("\nEnter the name of the player : ").title()
        plr=PlayerStats(player)
        p1=plr.getstats()
        if p1!=99:
            disp=DisplayInfo()
            disp.singlePlayer(plr)
    # Get two player names and display stats for option '2'
    elif choice=="2":
        player1=input("\nEnter the name of the first player : ").title()
        plr1=PlayerStats(player1)
        p1=plr1.getstats()
        if p1!=99 :
            player2=input("Enter the name of the second player : ").title()
            plr2=PlayerStats(player2)
            p2=plr2.getstats()
            if p2!=99:
                disp=DisplayInfo()
                disp.twoPlayer(plr1,plr2)
    elif choice=="3":
        break
    else:
        print("Please enter a right option")