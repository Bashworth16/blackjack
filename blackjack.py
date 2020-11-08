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
    if n == Rank.Two:
        return 2
    if n == Rank.Three:
        return 3
    if n == Rank.Four:
        return 4
    if n == Rank.Five:
        return 5
    if n == Rank.Six:
        return 6
    if n == Rank.Seven:
        return 7
    if n == Rank.Eight:
        return 8
    if n == Rank.Nine:
        return 9
    if n == Rank.Ten:
        return 10
    if n == Rank.Jack:
        return 10
    if n == Rank.Queen:
        return 10
    if n == Rank.King:
        return 10


def main():
    deck = make_deck()
    random.shuffle(deck)
    hand = []

    the_house = []
    dealer_card = deal(deck)
    the_house.append(dealer_card)
    house_total = card_point(dealer_card)

    # add_to_hand(dealt_card)
    dealt_card = deal(deck)
    hand.append(dealt_card)
    total = card_point(dealt_card)

    # "Play Loop"
    play = True
    while play:
        print(f'Player 1: {hand}')
        print(f'The House: {the_house}')
        print("")

        # get_hos is "Hit or Stay".
        get_hos = input(f'Your Total is {total} and The House has {house_total}, would you like to Hit? ("y" or "n"): ')

        print("")

        # if get_hos is 'y' both player 1 and The House take cards. If 'n' then only The House takes a card. #Beta Version haha
        if get_hos == 'y':

            d = deal(deck)
            hd = deal(deck)

            hand.append(d)
            the_house.append(hd)

            total += card_point(d)
            house_total += card_point(hd)

        if get_hos == 'n':
            hd = deal(deck)
            the_house.append(hd)
            house_total += card_point(hd)

        # Evaluates point for both players to determine a winner and a loop break condition. If a break condition is not met, continue to beginning of "Play Loop".
        if total == 21 and house_total != 21:
            print(f'{hand, total}')
            print('YOU WIN!')
            break
        if house_total == 21 and total != 21:
            print(f'{house_total, the_house}: House wins!')
            print("")
            break
        if total > 21 and house_total < 21:
            print(total)
            print('Bust! House Wins')
            break
        if house_total > 21 and total < 21:
            print(house_total)
            print('House Busts! Player 1 Wins!')
            print("")
            break
        if total > 21 and house_total > 21:
            print(f'Player has {total} and House has {house_total}, both players Bust!')
            if __name__ == "__main__":
                main()
        else:
            continue

    # "Leaving Loop": Ask players if they want to play again or not. I am using 'else' instead of "try/except" to get around value errors.
    leaving = True
    while leaving:
        play_again = input("Would you like to play again? ('y' or 'n'): ")
        if play_again == 'y':
            leaving = False
            if __name__ == "__main__":
                main()
        if play_again == 'n':
            print('Goodbye!')
            break
        else:
            print('Please Choose "y" or "n"!')
            continue


if __name__ == "__main__":
    main()
