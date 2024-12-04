import game as g

g.initPlayers()

damageajip = int(input("masukkan damage ajip berapa: "))
damagevito = int(input("masukkan damage vito berapa: "))
damagehenry = int(input("masukkan damage henry berapa: "))
g.addPlayer(g.createNewPlayer('Ajip', damage=damageajip, defensePower=10))
g.addPlayer(g.createNewPlayer('Vito', damage=damagevito, defensePower=20))
g.addPlayer(g.createNewPlayer('Henry', damage=damagehenry, defensePower=5))


print(g.PlayerList)


g.displayMatchResult()


g.attackPlayer(g.PlayerList[0], g.PlayerList[1])  # Ajip menyerang Vito
g.attackPlayer(g.PlayerList[1], g. PlayerList[2])  # Vito menyerang Henry

for i in g.PlayerList:
    if i["health"] == 0:
        print(f"{i['name']} telah terbunuh")
        print(f"{i['name']} has been defeated...")
        g.removePlayer(i['name'])


g.displayMatchResult()
print("Game Ended!")
