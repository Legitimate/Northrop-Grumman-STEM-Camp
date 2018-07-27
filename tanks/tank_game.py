# Tank Game using our Tank Class

from tank import Tank
# Game setup
tanks = {}
numPlayers = int(input("How many players? "))
for player in range(1, numPlayers+1):
    printString = "Player " + str(player) + "'s name: "
    tanks[player] = Tank( input(printString) )

aliveTanks = len(tanks)

while aliveTanks > 1:
    # List the tanks and their stats
    print()
    for playerNum in tanks.keys():
        print(playerNum, tanks[playerNum])
