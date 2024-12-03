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
        defensePower=defensePower,
        health=100,
        defense=False
    )


# nomor 3
def addPlayer(player):
    PlayerList.append(player)


# nomor 4
def removePlayer(name):
    for player in PlayerList:
        if player['name'] == name:
            PlayerList.remove(player)
            return True
        else:
            return print("error")

# nomor 5


def setPlayer(player, key, value):
    player[key] = value

# nomor 6


def attackPlayer(attacker, target):
    if attacker['defense'] == True:
        damaged = max(0, attacker['damage'] - target['defensePower'])
        setPlayer(attacker, 'score', attacker['score'] + 0.8)

    else:
        damaged = attacker['damage']
        setPlayer(attacker, 'score', attacker['score'] + 1)

    setPlayer(target, 'health', target['health'] - damaged)
    setPlayer(target, 'defense', False)

    # nomor 7


def sorting(x):
    return -x['score'], -x['health']


def displayMatchResult():
    PlayerList.sort(key=sorting(PlayerList))
    for i, player in enumerate(PlayerList, 1):
        # ini blm ada counternya wlee harusnya kek gini
        print(
            f"Rank {i}: {player['name']} | Score: {player['score']} | health: {player['health']}")

    # "Rank 1: Player2 | Score: 70 | Health: 100",
    # "Rank 2: Player3 | Score: 70 | Health: 90",
    # "Rank 3: Player1 | Score: 50 | Health: 100"
    return PlayerList
