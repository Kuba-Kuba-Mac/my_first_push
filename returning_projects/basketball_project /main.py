# basketball player states but with OOP
class Player():
    def __init__(self, name, score, assists, rebound):
        self.name = name
        self.score = score
        self.assists = assists
        self.rebound = rebound
        self.players = []

    def add_player(self, name, score, assists, rebound):
        self.players.append({
        "name": name,
        "score": score,
        "assists": assists,
        "rebound": rebound
        })

    def show_all(self):
        for i,x in enumerate(players,start=1):




s = Player("lebron",12,12,12,)
s.add_player("kuba",30,12,12)

