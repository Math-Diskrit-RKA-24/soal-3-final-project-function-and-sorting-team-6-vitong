PlayerList = []
# nomor 1


def initPlayers():
    global PlayerList
    PlayerList = []


# nomor 2
def createNewPlayer(name, damage=0, defensePower=0):
    return dict(
        name=name,
        score=0,
        damage=damage,
        health=100,
        defensePower=defensePower,
        defense=False)


# nomor 3
def addPlayer(player):
    PlayerList.append(player)


# nomor 4
def removePlayer(name):
    for player in PlayerList:
        if player['name'] == name:
            PlayerList.remove(player)
            return
    print("There is no player with that name!")

# nomor 5


def setPlayer(player, key, value):
    player[key] = value

# nomor 6


def attackPlayer(attacker, target):
    if target['defense'] == True:
        damaged = max(0, attacker['damage'] - target['defensePower'])
        setPlayer(attacker, 'score', attacker['score'] + 0.8)

    else:
        damaged = attacker['damage']
        setPlayer(attacker, 'score', attacker['score'] + 1)

    setPlayer(target, 'health', target['health'] - damaged)
    setPlayer(target, 'defense', False)

    # nomor 7


def displayMatchResult():
    PlayerList.sort(key=lambda y: (-y['score'], -y['health']))
    for i, player in enumerate(PlayerList, 1):

        print(
            f"Rank {i}: {player['name']} | Score: {player['score']} | Health: {player['health']}")

    return PlayerList

initPlayers()


addPlayer(createNewPlayer("Ajip", damage=20, defensePower=10))
addPlayer(createNewPlayer("Vito", damage=0, defensePower=20))
addPlayer(createNewPlayer("Henry", damage=10, defensePower=5))
removePlayer("Tono")


attackPlayer(PlayerList[0], PlayerList[1])  # Ajip menyerang Vito
attackPlayer(PlayerList[1], PlayerList[2])  # Vito menyerang Henry
attackPlayer(PlayerList[0], PlayerList[2]) #Ajip menyerang Henry


displayMatchResult()
