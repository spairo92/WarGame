import json
squadfile = "squad.json"
rosterfile = "roster.json"


def startGame():    #initial function
  answer1 = 1
  answer2 = 1
  while answer1:
      playGame = raw_input('Do you want to play a game?: [Y/N] \n')
      if playGame=='Y' or playGame == 'y':
          answer1 = 0
      elif playGame == 'N' or playGame == 'n':
          exit()
      else:
          print "Please choose either Y or N \n"
  while answer2:
      opponentType = raw_input("Enter Squad[1] or Create a new Squad[0] \n")
      if opponentType == '1':
          answer2 = 0
      elif opponentType == '0':
          print "Function under construction. Please use Squad number 1"
          answer2 = 1
      else:
          print "Please select a valid squad"

def printSquad():   #print id and type of squad members
    # load json data from team file
    squad_data = json.load(open(squadfile))
    # print (squad_data[0]['type'])
    print "My Squad: \nID\tMEMBER"
    for member in squad_data:
        print member['id']+"\t"+member['type']

def buyMember(money):   #adding member from roster file to squad file
    squad_data = json.load(open(squadfile))
    roster_data = json.load(open(rosterfile))

    select = raw_input("Choose member ID you want to buy [0-n] or [M] to go to Squad [M]enu \n")
    if select == 'M' or select == 'm':
        return money
    else:
        for member in roster_data:
            if member['id'] == select:
                cost = int(member['cost'])
                if cost < money or cost == money:
                    squad_data.append(member)
                    json.dump(squad_data, open(squadfile, 'w'))
                    money=money-int(member['cost'])
                    return money
                else:
                    print "We are sorry, you don't have enough money to buy this member"
                    raw_input("\nPress enter to go back to Squad Menu...")

# def buyMember2(money):
#     squad_data = json.load(open(squadfile))
#     roster_data = json.load(open(rosterfile))
#
#     select = raw_input("Choose member ID you want to buy [0-n] \n")
#     for member in roster_data:
#         if member['id'] == select:
#             squad_data.append(member)
#
#     json.dump(squad_data, open(squadfile, 'w'))
#     return money

def deleteMember():     #remove selected member from the squad
    squad_data = json.load(open(squadfile))
    select = raw_input("Choose member ID you want to delete [0-n] \n")
    sure = raw_input("Are you sure you want to delte this member?[Y/N]")
    if sure == 'Y' or sure == 'y':
        for i in xrange(len(squad_data)):
            if squad_data[i]["id"] == select:
                squad_data.pop(i)
                break
    elif sure == 'N' or sure == 'n':
        raw_input("Press enter to go to Squad Menu...")
    else:
        print "Please enter a valid answer"

    json.dump(squad_data, open(squadfile, 'w'))

def printSquadDetails():    #print all stats for squad members
    squad_data = json.load(open(squadfile))
    for member in squad_data:
        print "ID " + member['id'] + "\t" + member['type'] + " costing (" + member['cost'] + ")\t with stats: Move [" + \
              member['move'] + "] Fight [" \
              + member['fight'] + "] Shoot [" + member['shoot'] + "] Armour [" + member['armour'] + "] Morale [" + \
              member['morale'] + "] Health ]" + member['health'] \
              + "] Experience [" + member['experience'] + "] Specialism [" + member['specialism'] + "] Skills [" + \
              member['skills'] + "] Items [" + member['items'] + "]"

def printRoster():  #print all stats for roster members
    roster_data =  json.load(open(rosterfile))
    for member in roster_data:
        print "ID " + member['id'] + "\t" + member['type'] + " costing (" + member['cost'] + ")\t with stats: Move [" + \
              member['move'] + "] Fight [" \
              + member['fight'] + "] Shoot [" + member['shoot'] + "] Armour [" + member['armour'] + "] Morale [" + \
              member['morale'] + "] Health ]" + member['health'] \
              + "] Experience [" + member['experience'] + "] Specialism [" + member['specialism'] + "] Skills [" + \
              member['skills'] + "] Items [" + member['items'] + "]"

def updateStats():  #update experience
    squad_data = json.load(open(squadfile))
    for member in squad_data:
        if member['type'] == 'Captain' or member['type'] == 'Hierophant':
            hey = member['experience']
            hey2=int(hey)+1
            member['experience']=str(hey2)
    json.dump(squad_data, open(squadfile, 'w'))
