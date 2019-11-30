import random

player_turn = 0

class Won(Exception):
    def __init__(self,i):
        pass

class Player:
    def __init__(self):
        self.hand = [1,0,0,0]
        self.won = 0

    def link(self,game):
        self.game = game

    def play(self):
        pass

    def bid(self):
        pass

    def turn_cards(self):
        pass

    def lose(self):
        r = random.randint(0,len(self.hand)-1)
        del self.hand[r]

    def win(self):
        self.won += 1
        if self.won >= 2:
            raise Won(self)

class Game:
    def __init__(self,players):
        self.players = players
        self.played = [None]*len(players)
        self.best_bid = 0
        self.player_bid = None
        for p in players:
            p.link(self)

    def round(self):
        for i in range(len(self.players)):
            self.play(i)
        for i in range(len(self.players)):
            self.bid(i)
        bidder = self.players[self.player_bid]
        cards = bidder.turn_cards()
        print(self.player_bid,"turned",cards)
        if sum([self.played[i] for i in cards]) >= 1:
            print(self.player_bid,"lost round")
            bidder.lose()
        else:
            print(self.player_bid,"win round")
            bidder.win()
        
    def play(self,i):
        self.played[i] = self.players[i].play()
        print(i,"played",self.played[i])

    def bid(self,i):
        bid = self.players[i].bid()
        if bid > self.best_bid:
            print(i,"bet",bid)
            self.best_bid = bid
            self.player_bid = i
