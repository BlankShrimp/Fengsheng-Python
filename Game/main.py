from model.card import *;


def main():
    a = Card(0, Card.COLOR_BLUE, Card.TRANS_DIRECT, Card.CLOCKWISE, Card.UNLOCKED)
    # b = Gongkai(0, Card.COLOR_BLUE, Card.TRANS_DIRECT, Card.CLOCKWISE, Card.UNLOCKED)
    # b.cc = 1
    # print(b.cc)

    b = (1, a)
    print(b[1].color)
    b[1].color = Card.COLOR_RED
    print(b[1].color)

if __name__ == '__main__':
    main()