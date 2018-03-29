from game_functions import *
from random import choice
import json

if __name__ == '__main__':

    bank=50
    startGame()

    while True:
        print "Welcome in the WarGame! \n"

        printSquad()
        print "\nMy Money: ", bank



        playGame = raw_input('\nChoose Action: (Squad [S]tats, check [R]oster, [D]elete member, [B]attle, [E]xit) \nEnter Action:')
        if playGame == 'S' or playGame == 's':
            answer = 1
            printSquadDetails()
            raw_input("Press Enter to go back to the Squad Menu...")

        elif playGame == 'R' or playGame == 'r':
            printRoster()

            buy = raw_input("Do you want to buy any new member?")
            if buy == 'Y' or buy == 'y':
                buyMember()

        elif playGame == 'D' or playGame == 'd':
            deleteMember()

        elif playGame == 'B' or playGame == 'b':
            battle = choice(['win', 'lose'])
            if battle == 'win':
                bank=bank+10
                updateStats()
                print "Congratulations, you won!\nYour Money and Captain/Hierophant experience upgraded :) "
            elif battle == 'lose':
                print "Sorry, you lost the battle :( "

            raw_input("\nPress Enter to go back in the Squad Menu...")

        elif playGame == 'E' or playGame == 'e':
            exit()

        else:
            print "Please choose a valid option \n"


