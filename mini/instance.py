from mini import Player,Game

"""Creation of player """
class Player1(Player):
    def play(self):
        return self.hand[0]

    def bid(self):
        return 1

    def turn_cards(self):
        return [self.game.players.index(self)]

#Instances of players
playerA = Player1()
playerB = Player1()

#Creates the game
g = Game([playerA,playerB])

#Launch 2 rounds
g.round()
g.round()
