from mini import Player,Game

class Player1(Player):
    def play(self):
        return self.hand[0]

    def bid(self):
        return 1

    def turn_cards(self):
        return [self.game.players.index(self)]

playerA = Player1()
playerB = Player1()

g = Game([playerA,playerB])
g.round()
g.round()
