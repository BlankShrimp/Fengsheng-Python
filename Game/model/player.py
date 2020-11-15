class Player(object):
    TEAM_GREEN = 0
    TEAM_RED = 1
    TEAM_BLUE = 2

    def __init__(self, id, front_grey, front_red, front_blue, deck_grey, deck_red, deck_blue): 
        self.id = id
        self.front_grey = front_grey
        self.front_red = front_red
        self.front_blue = front_blue
        self.deck_grey = deck_grey
        self.deck_red = deck_red
        self.deck_blue = deck_blue