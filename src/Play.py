import game as g

g.initPlayers()

g.addPlayer(g.createNewPlayer('Ajip', damage=20, defensePower=10))
g.addPlayer(g.createNewPlayer('Vito', damage=0, defensePower=20))
g.addPlayer(g.createNewPlayer('Henry', damage=10, defensePower=5))
print(g.PlayerList)


g.displayMatchResult()

g.attackPlayer(g.PlayerList[0], g.PlayerList[1])  # Ajip menyerang Vito
g.attackPlayer(g.PlayerList[1],g. PlayerList[2])  # Vito menyerang Henry
g.attackPlayer(g.PlayerList[0], g.PlayerList[2])
print('Henry has been defeated...')  
g.removePlayer("Henry")


g.displayMatchResult()
print("Game Ended!")