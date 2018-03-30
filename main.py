from game_functions import *
from random import choice
import json

global money
if __name__ == '__main__':


    money = 70
    startGame()

    while True:
        print "Welcome in the WarGame! \n"

        printSquad()
        print "\nMy Money: ", money



        playGame = raw_input('\nChoose Action: (Squad [S]tats, check [R]oster, [D]elete member, [B]attle, [E]xit) \nEnter Action:')
        if playGame == 'S' or playGame == 's':
            answer = 1
            printSquadDetails()
            raw_input("Press Enter to go back to the Squad Menu...")

        elif playGame == 'R' or playGame == 'r':
            printRoster()

            buy = raw_input("Do you want to buy any new member?\n[Y]es or any other key to continue...")
            if buy == 'Y' or buy == 'y':
                money = buyMember(money)
                #money = buyMember2(money)
        elif playGame == 'D' or playGame == 'd':
            deleteMember()

        elif playGame == 'B' or playGame == 'b':
            battle = choice(['win', 'lose'])
            if battle == 'win':
                money=money+10
                updateStats()
                print "Congratulations, you won!\nYour Money and Captain/Hierophant experience upgraded :) "
            elif battle == 'lose':
                print "Sorry, you lost the battle :( "

            raw_input("\nPress Enter to go back in the Squad Menu...")

        elif playGame == 'E' or playGame == 'e':
            exit()

        else:
            print "Please choose a valid option \n"


