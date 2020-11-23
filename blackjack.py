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


def render_hand(x):
    ren_hand = ''
    for card in x:
        s = card.suit
        r = card.rank
        ren_card = ''
        if r == Rank.Ace:
            ren_card = "A"
        if r == Rank.Two:
            ren_card = '2'
        if r == Rank.Three:
            ren_card = '3'
        if r == Rank.Four:
            ren_card = '4'
        if r == Rank.Five:
            ren_card = '5'
        if r == Rank.Six:
            ren_card = '6'
        if r == Rank.Seven:
            ren_card = '7'
        if r == Rank.Eight:
            ren_card = '8'
        if r == Rank.Nine:
            ren_card = '9'
        if r == Rank.Ten:
            ren_card = '10'
        if r == Rank.Jack:
            ren_card = "J"
        if r == Rank.Queen:
            ren_card = "Q"
        if r == Rank.King:
            ren_card = "K"
        if s == Suit.Spades:
            ren_card += '♠ '
            ren_hand += ren_card
        if s == Suit.Hearts:
            ren_card += '♥ '
            ren_hand += ren_card
        if s == Suit.Diamonds:
            ren_card += '♦ '
            ren_hand += ren_card
        if s == Suit.Clubs:
            ren_card += '♣ '
            ren_hand += ren_card
    return ren_hand


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

# Evaluates point for both players to determine a winner and a loop break condition. If a break condition is
# not met, continue to beginning of "Play Loop".


def get_winner(pt, ph, ht, hh):
    if pt == 21 and ht == 21:
        print(f'The House: {hh}= {ht}')
        print(f'Player 1: {ph}= {pt} \n DOUBLE BLACKJACK!')
        return True
    if pt == 21 and ht != 21:
        print(f'The House: {render_hand(hh)}= {ht}')
        print(f'BLACKJACK! {render_hand(ph)}= {pt} \nYOU WIN!')
        return True
    if ht == 21 and pt != 21:
        print(f'Player 1: {render_hand(ph)}= {pt}')
        print(f'BLACKJACK! {render_hand(hh)}= {ht} \nHouse wins!')
        return True
    if ht < 21 < pt:
        print(f'The House: {render_hand(hh)}= {ht}')
        print(f'You Bust! {render_hand(ph)}= {pt} \nHouse Wins!')
        return True
    if ht > 21 > pt:
        print(f'Player 1: {render_hand(ph)}= {pt}')
        print(f'House Busts: {render_hand(hh)}= {ht} \nYou Win!')
        return True
    if pt > 21 and ht > 21:
        print(
            f'Player 1: {render_hand(ph)}= {pt} \nThe House: {render_hand(hh)}= {ht} \nboth players Bust!')
        print("")
        if __name__ == "__main__":
            main()

# get_hos is "Hit or Stay".


def get_hit_or_stay(t, ht):
    get_hos = input(f'Your Total is {t} and The House has {ht}, would you like to Hit? ("y" or "n"): ')
    return get_hos


def play_again():
    p = input("Would you like to play again? ('y' or 'n'): ")
    return p


def leaving(a):
    leave = True
    while leave:
        print("")
        if a == 'y':
            leave = False
            if __name__ == "__main__":
                main()
        if a == 'n':
            print('Goodbye!')
            exit()
        else:
            print('Please Choose "y" or "n"!')
            continue


def main():
    deck = make_deck()
    random.shuffle(deck)
    hand = []
    the_house = []

    dealer_card = deal(deck)
    dealer_card2 = deal(deck)
    the_house.append(dealer_card)
    the_house.append(dealer_card2)
    house_total = card_point(dealer_card)
    house_total += card_point(dealer_card2)

    # add_to_hand(dealt_card)
    dealt_card = deal(deck)
    dealt_card2 = deal(deck)
    hand.append(dealt_card)
    hand.append(dealt_card2)
    total = card_point(dealt_card)
    total += card_point(dealt_card2)

    # "Play Loop"
    play = True
    while play:
        print(f'Player 1: {render_hand(hand)}')
        print(f'The House: {render_hand(the_house)}')
        print("")

        winner = get_winner(total, hand, house_total, the_house)
        if winner:
            break

        get_hos = get_hit_or_stay(total, house_total)
        if get_hos == 'y':
            d = deal(deck)
            hd = deal(deck)
            hand.append(d)
            the_house.append(hd)
            total += card_point(d)
            house_total += card_point(hd)
        if get_hos == 'n':
            pass
        else:
            pass

    response = play_again()
    leaving(response)


if __name__ == "__main__":
    main()
