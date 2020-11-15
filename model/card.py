import _asyncio
import websocket


class Card(object):
    COLOR_GREY = 1
    COLOR_RED = 2
    COLOR_BLUE = 3

    TRANS_SECRET = 0
    TRANS_DIRECT = 1
    TRANS_PLAIN = 2

    CLOCKWISE = True
    COUNTER_CLOCKWISE = False

    LOCKED = True
    UNLOCKED = False

    def __init__(self, id, color, trans, clockwise, lock):
        self.id = id
        self.color = color
        self.trans = trans
        self.clockwise = clockwise
        self.lock = lock


class Gongkai(Card):
    def act(self, socket):
        pass