#!/usr/bin/python

import random

class GameFactory:
    factories = {}

    def add_factory(id, factory):
        GameFactory.factories[id] = factory
    add_factory = staticmethod(add_factory)
    
    def create_game(id):
        return GameFactory.factories[int(id)].create()
    create_game = staticmethod(create_game)

class Game_Default:
    description = "Standard rock, paper, scissors game"
    def __init__(self):
        self.options = { 'r' : '[r]ock', 'p' : '[p]aper', 's' : '[s]cissors'}

    def decide(self, p1, p2):
        print "(%s) %s vs %s (%s)" % ( p1.name, self.options[p1.choice], self.options[p2.choice], p2.name )
        pair = (p1.choice, p2.choice)
        result = { pair == ('p', 'p') or pair == ('r', 'r') or pair == ('s', 's'): False,
                   pair == ('p', 'r') or pair == ('r', 's') or pair == ('s', 'p'): p1,
                   pair == ('p', 's') or pair == ('r', 'p') or pair == ('s', 'r'): p2 }[1]
        return result
    def create(): return Game_Default()
    create = staticmethod(create)

class Game_Batman:
    description = "Rock, paper, scissors, and Batman. well, it's batman. enough said."
    def __init__(self):
        self.options = { 'r' : '[r]ock', 'p' : '[p]aper', 's' : '[s]cissors', 'b' : '[b]atman'}

    def decide(self, p1, p2):
        print "(%s) %s vs %s (%s)" % ( p1.name, self.options[p1.choice], self.options[p2.choice], p2.name )
        pair = (p1.choice, p2.choice)
        if ( p1.choice == 'b' or p2.choice == 'b' ):
            return p1 if p1.choice == 'b' else p2
        else:
            result = { pair == ('p', 'p') or pair == ('r', 'r') or pair == ('s', 's'): False,
                       pair == ('p', 'r') or pair == ('r', 's') or pair == ('s', 'p'): p1,
                       pair == ('p', 's') or pair == ('r', 'p') or pair == ('s', 'r'): p2 }[1]
            return result
    def create(): return Game_Batman()
    create = staticmethod(create)

class Game_Phil_Style:
    description = "Phil's weird version of rock, paper and scissors."
    def __init__(self):
        self.options = { 'r' : '[r]ock', 'p' : '[p]aper', 's' : '[s]cissors', 'l' : '[l]izzard', 'k' : 'spoc[k]' }

    def decide(self, p1, p2):
        print "(%s) %s vs %s (%s)" % ( p1.name, self.options[p1.choice], self.options[p2.choice], p2.name )
        
	return random.choice([p1,p2])
    def create(): return Game_Phil_Style()
    create = staticmethod(create)

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.choice = 0

class Game:
    def __init__(self, type):
	self.players = []
        self.cpu = Player("Computer")
        self.type = type
    def initialise(self):
        self.count = raw_input("Select number of players:")
	if (self.count.isdigit()):
            for i in range(1, int(self.count) + 1):
                name = raw_input("Player %d name: " % i )
                self.players.append( Player(name) )
   
    def player_selection(self, player):
        selected = ''
        while selected not in self.type.options.keys():
            for option in self.type.options.values():
                print option
            raw  = raw_input("Player:%s " % player.name)
            if ( raw ):
                selected = raw[0]
        return selected
   
    def scores(self):
        print ""
        print "******** Score Board ********"
        print "Name\t\t\tScore"
        print "%s\t\t%d" % ( self.cpu.name, self.cpu.wins)
	for player in self.players:
            print "%s\t\t\t%d" % ( player.name, player.wins)
        print ""

    def start(self):
        while True:
           for player in self.players:
               player.choice = self.player_selection(player)
               self.cpu.choice = random.choice(self.type.options.keys())
               winner = self.type.decide(player, self.cpu)
               if ( winner ):
                   winner.wins += 1
                   print "%s WINS - %d" % (winner.name, winner.wins)
                   
               else:
                   print "Draw..."
               self.scores()

# Construct our factory
GameFactory.add_factory(0, Game_Default)
GameFactory.add_factory(1, Game_Batman)
GameFactory.add_factory(2, Game_Phil_Style)

game_type = -1
while int(game_type) not in range(0, len(GameFactory.factories)):
    print "* * * G A M E  * S E L E C T * * *"
    for x in range(0, len(GameFactory.factories)):
        print "%d\t%s" % (x, GameFactory.factories[x].description)
    game_type = raw_input("Please select a game type.")
    if not game_type or not game_type.isdigit(): game_type = -1
    

game = Game(GameFactory.create_game(game_type))
game.initialise()
game.start()
