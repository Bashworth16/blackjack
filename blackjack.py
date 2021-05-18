#!/usr/bin/env python

import enum
import random
from typing import List


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
        return f"<Card({self.rank.name}, {self.suit.name})>"


class GameState:
    def __init__(self, deck: List[Card], player_hand: List[Card], dealer_hand: List[Card]):
        self.deck = deck
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand

    def deal(self):
        """Removes and returns first card of the deck."""
        return self.deck.pop(0)


def make_deck():
    deck = []
    for suit in Suit:
        for rank in Rank:
            card = Card(rank, suit)
            deck.append(card)
    return deck


def house_hit(state: GameState):
    while hand_total(state.dealer_hand) < 17:
        state.dealer_hand.append(state.deal())


def hit_player(state: GameState):
    state.player_hand.append(state.deal())


# TODO This function does too much!
def hit(hit_response, state: GameState):
    if hit_response == 'y':
        hit_player(state)
    elif hit_response == 'n':
        house_hit(state)
    else:
        print("Please choose 'y' or 'n'")
        get_hit_or_stay(state)


def hand_total(hand):
    total = 0
    ace_count = 0

    # Evaluate card points and add them to total.
    for card in hand:
        r = card.rank
        total += card_point(card)
        if r == Rank.Ace:
            ace_count += 1
        while ace_count > 0 and total > 21:
            ace_count -= 1
            total -= 10
    return total


def initial_deal(state):
    state.player_hand.append(state.deal())
    state.player_hand.append(state.deal())
    state.dealer_hand.append(state.deal())
    state.dealer_hand.append(state.deal())


# Output
def show_cards(state: GameState):
    print(f'Player 1: {render_hand(state.player_hand)}')
    print(f'The House: {render_dealer(state.dealer_hand)}\n')


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


# IO TODO separate printing and winner logic.
def get_winner(state: GameState):
    player_total = hand_total(state.player_hand)
    house_total = hand_total(state.dealer_hand)
    if player_total == 21 and house_total == 21:
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n House Wins!')
        return True
    if player_total == 21 and house_total != 21:
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'BLACKJACK! {render_hand(state.player_hand)}= {player_total} \nYOU WIN!')
        return True
    if house_total == 21 and player_total != 21:
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total}')
        print(f'BLACKJACK! {render_hand(state.dealer_hand)}= {house_total} \nHouse wins!')
        return True
    if house_total < 21 < player_total:
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'You Bust! {render_hand(state.player_hand)}= {player_total} \nHouse Wins!')
        return True
    if house_total > 21 > player_total:
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total}')
        print(f'House Busts: {render_hand(state.dealer_hand)}= {house_total} \nYou Win!')
        return True
    if player_total > 21 and house_total > 21:
        print(
            f'Player 1: {render_hand(state.player_hand)}= {player_total} \nPlayers 1 Busts!')
        print("")
    if player_total < house_total < 21:
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n House Wins!')
        return True
    if player_total > house_total < 21 and house_total > 17:
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n YOU Win!')
        return True
    if __name__ == "__main__":
        main()


# TODO parse yes or no and return true or false instead of string if the user gives
# TODO an invalid input re-ask for
def get_hit_or_stay(state: GameState):
    total = hand_total(state.player_hand)
    get_hos = input(f'Your Total is {total}, would you like to Hit? ("y" or "n"): ')
    print("")
    return get_hos


# IO
def play_again():
    leaving = True
    while leaving:
        a = input("Would you like to play again? ('y' or 'n'): ")
        print("")
        if a == 'y':
            leaving = False
            if __name__ == "__main__":
                main()
        elif a == 'n':
            print('Goodbye!')
            exit()
        else:
            print('Please Choose "y" or "n"!')
            continue


# TODO Separate IO and logic
def has_blackjack(hand: List[Card]):
    total = hand_total(hand)
    if total != 21:
        return False
    if total == 21:
        return True


def main():
    state = GameState(deck=make_deck(), player_hand=[], dealer_hand=[])
    random.shuffle(state.deck)
    initial_deal(state)

    play = True
    while play:
        show_cards(state)
        if has_blackjack(state.player_hand):
            print(f'YOU GOT A BLACKJACK!')
            break

        hit_or_not = get_hit_or_stay(state)
        hit(hit_or_not, state)

        total = hand_total(state.player_hand)

        if hit_or_not == 'y' and total < 21:
            continue

        winner = get_winner(state)
        if winner:
            break

    play_again()


if __name__ == "__main__":
    main()
