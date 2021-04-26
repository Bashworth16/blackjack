#!/usr/bin/env python

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


def render_dealer(x):
    first_card = "🂠 "
    ren_hand = ''
    for card in x[1:]:
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

    return first_card + ren_hand


def card_count(x):
    return len(x)


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


def get_winner(player_total, player_hand, house_total, house_hand):
    if player_total == 21 and house_total == 21:
        print(f'The House: {render_hand(house_hand)}= {house_total}')
        print(f'Player 1: {render_hand(player_hand)}= {player_total} \n House Wins!')
        return True
    if player_total == 21 and house_total != 21:
        print(f'The House: {render_hand(house_hand)}= {house_total}')
        print(f'BLACKJACK! {render_hand(player_hand)}= {player_total} \nYOU WIN!')
        return True
    if house_total == 21 and player_total != 21:
        print(f'Player 1: {render_hand(player_hand)}= {player_total}')
        print(f'BLACKJACK! {render_hand(house_hand)}= {house_total} \nHouse wins!')
        return True
    if house_total < 21 < player_total:
        print(f'The House: {render_hand(house_hand)}= {house_total}')
        print(f'You Bust! {render_hand(player_hand)}= {player_total} \nHouse Wins!')
        return True
    if house_total > 21 > player_total:
        print(f'Player 1: {render_hand(player_hand)}= {player_total}')
        print(f'House Busts: {render_hand(house_hand)}= {house_total} \nYou Win!')
        return True
    if player_total > 21 and house_total > 21:
        print(
            f'Player 1: {render_hand(player_hand)}= {player_total} \nPlayers 1 Busts!')
        print("")
    if player_total < house_total < 21:
        print(f'The House: {render_hand(house_hand)}= {house_total}')
        print(f'Player 1: {render_hand(player_hand)}= {player_total} \n House Wins!')
        return True
    if player_total > house_total < 21:
        print(f'The House: {render_hand(house_hand)}= {house_total}')
        print(f'Player 1: {render_hand(player_hand)}= {player_total} \n YOU Win!')
        return True
    if __name__ == "__main__":
        main()


def house_hit(house_total, house_hand, deck):
    while house_total < 17:
        x = deal(deck)
        house_hand.append(x)
        house_total += hand_total(house_hand)


def hit_player(total, hand, deck):
    x = deal(deck)
    hand.append(x)
    total += hand_total(hand)


def hit(hit_response, total, hand, deck, house_total, house_hand):
    h = hit_response
    if h == 'y':
        hit_player(total, hand, deck)
    elif h == 'n':
        house_hit(house_total, house_hand, deck)
    else:
        print("Please choose 'y' or 'n'")
        get_hit_or_stay(total)


def get_hit_or_stay(total):
    get_hos = input(f'Your Total is {total}, would you like to Hit? ("y" or "n"): ')
    print("")
    return get_hos


def play_again():
    leaving = True
    while leaving:
        a = input("Would you like to play again? ('y' or 'n'): ")
        print("")
        if a == 'y':
            leaving = False
            if __name__ == "__main__":
                main()
        if a == 'n':
            print('Goodbye!')
            exit()
        else:
            print('Please Choose "y" or "n"!')
            continue


def hand_total(hand):
    total = 0

    # Evaluate card points and add them to total.
    for card in hand:
        r = card.rank
        total += card_point(card)

        # If an Ace (11) would cause a bust, change to 1. If not Ace remains 11.
        if r == Rank.Ace and total > 21:
            total -= 10

    if total > 21:
        total = 0
        for card in hand:
            points = card_point(card)
            total += points
            x = card.rank
            if x == Rank.Ace:
                total -= 10
    return total


def show_cards(p, h):
    print(f'Player 1: {render_hand(p)}')
    print(f'The House: {render_dealer(h)}')
    print("")


def initial_deal(d, h, th):
    count = 0
    while count < 2:
        count += 1
        h.append(deal(d))
        th.append(deal(d))


def check_blackjack(total):
    if total != 21:
        return True
    if total == 21:
        print(f'{total} BLACKJACK!')
        return False


def main():
    deck = make_deck()
    random.shuffle(deck)
    hand = []
    the_house = []

    initial_deal(deck, hand, the_house)
    total = hand_total(hand)
    house_total = hand_total(the_house)
    # "Play Loop"
    play = True
    while play:
        # Displays cards to player.
        show_cards(hand, the_house)

        # If blackjack is dealt on the first hand the player is declared winner and the play cycle is broken.
        # this stops the game from asking if you want to hit or not after a blackjack has already been dealt.
        if check_blackjack(total) == False:
            break

        # Gets user input to hit or not on line 292. Total is used as an arg to display the total in the message.
        hit_or_not = get_hit_or_stay(total)

        # Line 274 The users input from hit_or_not is passed as the first arg.
        #       if the input == y, a new card is added tp
        #       hand and the points are totaled at card_point(x) on line 184.
        #       if the input == n, we use the 5th arg house_hit(house_total) line 269 to see
        #       if the house is below 16 points and should take cards.
        #       if it is neither, hit() asks for the proper input.
        #       other args are used for dealing new cards and adding them to the players hands.
        hit(hit_or_not, total, hand, deck, house_total, the_house)

        # Gets the players totals with retotal() on line 315
        total = hand_total(hand)
        house_total = hand_total(the_house)

        # If the player is asking for more cards, continue loop, don't check for winner
        if hit_or_not == 'y' and total < 21:
            continue

        # Compares players totals to determine a winner. hand args are passed for the winner display message.
        winner = get_winner(total, hand, house_total, the_house)
        if winner:
            break

    play_again()


if __name__ == "__main__":
    main()
