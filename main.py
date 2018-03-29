from game_functions import *
import json

if __name__ == '__main__':

    bank=500
    startGame()

    while True:
        print "Welcome in the WarGame! \n"

        printSquad()
        print "\nMy Money: ", bank



        playGame = raw_input('\nChoose Action: (Squad [S]tats, check [R]oster, [D]elete member, [B]attle, [E]xit) \nEnter Action:')
        if playGame == 'S' or playGame == 's':
            answer = 1
            printSquadDetails()
        elif playGame == 'R' or playGame == 'r':
            printRoster()

            buy = raw_input("Do you want to buy any new member?")
            if buy == 'Y' or buy == 'y':
                buyMember()



        elif playGame == 'D' or playGame == 'd':
            deleteMember()
        elif playGame == 'B' or playGame == 'b':
            answer = 0
        elif playGame == 'E' or playGame == 'e':
            exit()
        else:
            print "\t \t Please choose a valid option \n"


