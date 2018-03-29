import json
squadfile = "jsondata2/squad.json"
rosterfile = "jsondata2/roster.json"

def startGame():
  answer1 = 1
  answer2 = 1
  while answer1:
      playGame = raw_input('Do you want to play a game?: \n')
      if playGame=='Y' or playGame == 'y':
          answer1 = 0
      elif playGame == 'N' or playGame == 'n':
          exit()
      else:
          print "\t \t Please choose either Y or N \n"
  while answer2:
      opponentType = raw_input("Enter Squad[1] or Create a new Squad[0] \n")
      if opponentType == '1':
          answer2 = 0
      elif opponentType == '0':
          print "Function under construction. Please use Squad number 1"
          answer2 = 1
      else:
          print "Please select a valid squad"

def printSquad():
    # load json data from team file
    squad_data = json.load(open(squadfile))
    # print (data[0]['type'])
    print "My Squad: \nID\tMEMBER"
    for member in squad_data:
        #if member['id'] == '1':
            print member['id']+"\t"+member['type']

def buyMember():
    squad_data = json.load(open(squadfile))
    roster_data = json.load(open(rosterfile))

    select = raw_input("Choose member ID you want to buy [0-n] \n")
    for member in roster_data:
        if member['id'] == select:
            squad_data.append(member)

    json.dump(squad_data, open(squadfile, 'w'))

def deleteMember():
    squad_data = json.load(open(squadfile))

    select = raw_input("Choose member ID you want to delete [0-n] \n")


    for i in xrange(len(squad_data)):
        if squad_data[i]["id"] == select:
            squad_data.pop(i)
            break

    json.dump(squad_data, open(squadfile, 'w'))

def printSquadDetails():
    squad_data = json.load(open(squadfile))
    for member in squad_data:
        print "ID " + member['id'] + "\t" + member['type'] + " costing (" + member['cost'] + ")\t with stats: Move [" + \
              member['move'] + "] Fight [" \
              + member['fight'] + "] Shoot [" + member['shoot'] + "] Armour [" + member['armour'] + "] Morale [" + \
              member['morale'] + "] Health ]" + member['health'] \
              + "] Experience [" + member['experience'] + "] Specialism [" + member['specialism'] + "] Skills [" + \
              member['skills'] + "] Items [" + member['items'] + "]"

def printRoster():
    roster_data =  json.load(open(rosterfile))
    for member in roster_data:
        print "ID " + member['id'] + "\t" + member['type'] + " costing (" + member['cost'] + ")\t with stats: Move [" + \
              member['move'] + "] Fight [" \
              + member['fight'] + "] Shoot [" + member['shoot'] + "] Armour [" + member['armour'] + "] Morale [" + \
              member['morale'] + "] Health ]" + member['health'] \
              + "] Experience [" + member['experience'] + "] Specialism [" + member['specialism'] + "] Skills [" + \
              member['skills'] + "] Items [" + member['items'] + "]"

def updateStats():
    squad_data = json.load(open(squadfile))
    for member in squad_data:
        if member['type'] == 'Captain' or member['type'] == 'Hierophant':
            hey = member['experience']
            hey2=int(hey)+50
            member['experience']=str(hey2)
    json.dump(squad_data, open(squadfile, 'w'))
