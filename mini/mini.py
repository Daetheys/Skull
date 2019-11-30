import random

player_turn = 0

class Won(Exception):
    def __init__(self,i):
        pass

class Player:
    """ Player class """
    def __init__(self):
        self.hand = [1,0,0,0] #1-> Skull // 0-> Flower
        self.won = 0

    def link(self,game):
        #Have a link to the game configuration
        self.game = game

    def play(self): #To define -> play a card (0 or 1)
        pass

    def bid(self): #To define -> bid 
        pass

    def turn_cards(self): #To define -> Turn cards (needs to be the same number of cards than the last bid and start with cards of this player
        pass

    def lose(self): #Player loses
        r = random.randint(0,len(self.hand)-1)
        del self.hand[r]

    def win(self): #Player wins
        self.won += 1
        if self.won >= 2:
            raise Won(self)

class Game:
    """ Game class """
    def __init__(self,players):
        self.players = players
        self.played = [None]*len(players)
        self.best_bid = 0
        self.player_bid = None
        for p in players:
            p.link(self)

    def round(self):
        """ Start a round """
        #Play round
        for i in range(len(self.players)):
            self.play(i)
        #Bid round
        for i in range(len(self.players)):
            self.bid(i)
        #Get result of bid and turn cards
        bidder = self.players[self.player_bid]
        cards = bidder.turn_cards()
        print(self.player_bid,"turned",cards)
        #Verify if the bidder wins or loses
        if sum([self.played[i] for i in cards]) >= 1:
            print(self.player_bid,"lost round")
            bidder.lose()
        else:
            print(self.player_bid,"win round")
            bidder.win()
        
    def play(self,i):
        """ i will play """
        self.played[i] = self.players[i].play()
        print(i,"played",self.played[i])

    def bid(self,i):
        """ i will bid """
        bid = self.players[i].bid()
        if bid > self.best_bid:
            print(i,"bet",bid)
            self.best_bid = bid
            self.player_bid = i
