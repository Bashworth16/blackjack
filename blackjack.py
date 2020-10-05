import enum
import random


class Suit(enum.Enum):
    Clubs = enum.auto()
    Hearts = enum.auto()
    Spades = enum.auto()
    Diamonds = enum.auto()


class Rank(enum.Enum):
    Ace = enum.auto()
    Two = enum.auto()
    Three = enum.auto()
    Four = enum.auto()
    Five = enum.auto()
    Six = enum.auto()
    Seven = enum.auto()
    Eight = enum.auto()
    Nine = enum.auto()
    Ten = enum.auto()
    Jack = enum.auto()
    Queen = enum.auto()
    King = enum.auto()


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        # return "<Card(" + self.rank.name + ", " + self.suit.name + ")>"
        # return "<Card({0}, {1})>".format(self.rank.name, self.suit.name)
        return f"<Card({self.rank.name}, {self.suit.name})>"


def make_deck():
    deck = []
    for suit in Suit:
        for rank in Rank:
            card = Card(rank, suit)
            deck.append(card)
    return deck


def deal(d):
    """Removes and returns first card of the deck."""
    return d.pop(0)


def card_point(x):
    n = x.rank
    if n == Rank.Ace:
        return 11
    if n == "Two":
        return 2
    if n == "Three":
        return 3
    if n == "Four":
        return 4
    if n == "Five":
        return 5
    if n == "Six":
        return 6
    if n == "Seven":
        return 7
    if n == "Eight":
        return 8
    if n == "Nine":
        return 9
    if n == "Ten":
        return 10
    if n == "Jack":
        return 10
    if n == "Queen":
        return 10
    if n == "King":
        return 10


def main():
    deck = make_deck()
    random.shuffle(deck)
    hand = []

    dealt_card = deal(deck)
    hand.append(dealt_card)

    #add_to_hand(dealt_card)

    total = card_point(dealt_card)

    print(deck)
    print(len(deck))
    print(dealt_card)
    print(hand)
    print(total)

if __name__ == "__main__":
    main()
