#!/usr/bin/env python
import random
import enum
from typing import List, Optional


class Conclusion(enum.Enum):
    # noinspection PyArgumentList
    Push = enum.auto()
    # noinspection PyArgumentList
    PlayerBj = enum.auto()
    # noinspection PyArgumentList
    HouseBj = enum.auto()
    # noinspection PyArgumentList
    PlayerBust = enum.auto()
    # noinspection PyArgumentList
    HouseBust = enum.auto()
    # noinspection PyArgumentList
    PlayerWin = enum.auto()
    # noinspection PyArgumentList
    HouseWin = enum.auto()


class Play(enum.Enum):
    # noinspection PyArgumentList
    Hit = enum.auto()
    # noinspection PyArgumentList
    Stay = enum.auto()
    # noinspection PyArgumentList
    Split = enum.auto()


class Suit(enum.Enum):
    # noinspection PyArgumentList
    Clubs = enum.auto()
    # noinspection PyArgumentList
    Hearts = enum.auto()
    # noinspection PyArgumentList
    Spades = enum.auto()
    # noinspection PyArgumentList
    Diamonds = enum.auto()


class Rank(enum.Enum):
    # noinspection PyArgumentList
    Ace = enum.auto()
    # noinspection PyArgumentList
    Two = enum.auto()
    # noinspection PyArgumentList
    Three = enum.auto()
    # noinspection PyArgumentList
    Four = enum.auto()
    # noinspection PyArgumentList
    Five = enum.auto()
    # noinspection PyArgumentList
    Six = enum.auto()
    # noinspection PyArgumentList
    Seven = enum.auto()
    # noinspection PyArgumentList
    Eight = enum.auto()
    # noinspection PyArgumentList
    Nine = enum.auto()
    # noinspection PyArgumentList
    Ten = enum.auto()
    # noinspection PyArgumentList
    Jack = enum.auto()
    # noinspection PyArgumentList
    Queen = enum.auto()
    # noinspection PyArgumentList
    King = enum.auto()


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"<Card({self.rank.name}, {self.suit.name})>"


class Hand:
    def __init__(self):
        self.cards: List[Card] = []


class Coin(enum.Enum):
    # noinspection PyArgumentList
    Coin = enum.auto()


class Player:
    def __init__(self):
        self.hands = [Hand()]
        self.current_hand_index = 0
        self.coins = [Coin(1)]

    def make_coin_bag(self):
        while self.coins.count(Coin.Coin) < 100:
            self.coins.append(Coin.Coin)
        return list.count(self.coins, Coin.Coin)

    def active_hand(self):
        return self.hands[self.current_hand_index]


class Dealer:
    def __init__(self):
        self.hand = Hand()


class GameState:
    def __init__(self, deck: List[Card], player: Player, dealer: Dealer):
        self.deck = deck
        self.player = player
        self.dealer = dealer

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
    while hand_total(state.dealer.hand.cards) <= 17:
        state.dealer.hand.cards.append(state.deal())
    return


def hit_player(hand: Hand, state: GameState):
    return hand.cards.append(state.deal())


def hit(hit_response, state: GameState, hand):
    if hit_response == Play.Hit:
        hit_player(hand, state)
        return
    if hit_response == Play.Stay:
        house_hit(state)
        return
    raise ValueError(f"Invalid Play: {hit_response}")


def hand_total(hand):
    total = 0
    ace_count = 0
    for card in hand:
        r = card.rank
        total += card_point(card)
        if r == Rank.Ace:
            ace_count += 1
        while ace_count > 0 and total > 21:
            ace_count -= 1
            total -= 10
    return total


def initial_deal(state: GameState):
    state.player.active_hand().cards.append(state.deal())
    state.dealer.hand.cards.append(state.deal())
    state.player.active_hand().cards.append(state.deal())
    state.dealer.hand.cards.append(state.deal())
    return


def render_rank(card):
    r = card.rank
    if r == Rank.Ace:
        return "A"
    if r == Rank.Two:
        return '2'
    if r == Rank.Three:
        return '3'
    if r == Rank.Four:
        return '4'
    if r == Rank.Five:
        return '5'
    if r == Rank.Six:
        return '6'
    if r == Rank.Seven:
        return '7'
    if r == Rank.Eight:
        return '8'
    if r == Rank.Nine:
        return '9'
    if r == Rank.Ten:
        return '10'
    if r == Rank.Jack:
        return "J"
    if r == Rank.Queen:
        return "Q"
    if r == Rank.King:
        return "K"


def render_suit(card):
    if card.suit == Suit.Spades:
        return '♠ '
    if card.suit == Suit.Hearts:
        return '♥ '
    if card.suit == Suit.Diamonds:
        return '♦ '
    if card.suit == Suit.Clubs:
        return '♣ '


def render_card(ren_rank, ren_suit):
    return ren_rank + ren_suit


def render_hand(x):
    ren_hand = ''
    for card in x:
        ren_hand += render_card(render_rank(card), render_suit(card))
    return ren_hand


def render_dealer(x):
    first_card = "🂠 "
    ren_hand = ''
    for card in x.cards[1:]:
        ren_hand += render_card(render_rank(card), render_suit(card))
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


def get_winner(state: GameState, hand) -> Conclusion:
    house_total = hand_total(state.dealer.hand.cards)
    player_total = hand_total(hand.cards)
    if player_total == house_total:
        return Conclusion.Push
    if player_total > 21:
        return Conclusion.PlayerBust
    if house_total > 21:
        return Conclusion.HouseBust
    if player_total == 21:
        return Conclusion.PlayerBj
    if house_total == 21:
        return Conclusion.HouseBj
    if player_total < house_total:
        return Conclusion.HouseWin
    if player_total > house_total:
        return Conclusion.PlayerWin
    raise ValueError(f'Winner Inconclusive for {player_total} vs {house_total}')


def parse_play(s: str) -> Optional[Play]:
    if s == 'y':
        return Play.Hit
    if s == 'n':
        return Play.Stay
    return None


def has_blackjack(hand: Hand):
    total = hand_total(hand.cards)
    if total == 21:
        return True
    else:
        return False


def check_deck(state):
    if len(state.deck) < 25:
        return True
    else:
        return False


def set_table(state: GameState, cb=list):
    if check_deck(state) is True:
        state.deck = make_deck()
        state.player = Player()
        state.dealer = Dealer()
        random.shuffle(state.deck)
        initial_deal(state)
        state.player.coins = cb
        return
    else:
        state.player = Player()
        state.dealer = Dealer()
        initial_deal(state)
        state.player.coins = cb
        return


# For split_hand feature...
def split_hand(state: GameState):
    new_hand = Hand()
    split_card = state.player.active_hand().cards.pop(1)
    new_hand.cards.append(split_card)
    state.player.hands.append(new_hand)
    for hands in state.player.hands:
        hands.cards.append(state.deal())


def check_split(state):
    if len(state.player.active_hand().cards) > 2:
        return False
    if len(state.player.hands) > 1:
        return False
    for hands in state.player.hands:
        if card_point(hands.cards[1]) == \
                card_point(hands.cards[0]):
            return True
        else:
            return False


# For split_hand feature...
def check_for_bust(hand):
    if hand_total(hand) > 21:
        return True
    else:
        return False


def check_blackjack_or_bust(hand):
    if has_blackjack(hand):
        return Play.Stay
    if check_for_bust(hand.cards) is True:
        return Play.Stay
    else:
        return None


def check_bet(bet, state):
    if 0 < len(bet) < len(state.player.coins):
        return True
    if len(bet) < 0 or len(bet) > len(state.player.coins):
        return False


def bet_tally(bet, state: GameState):
    lose = [Conclusion.HouseBj, Conclusion.HouseWin, Conclusion.PlayerBust]
    win = [Conclusion.PlayerBj, Conclusion.PlayerWin, Conclusion.HouseBust]
    conclusion = get_winner(state, state.player.active_hand())
    for each in lose:
        if conclusion is each:
            for coin in bet:
                state.player.coins.remove(Coin(coin))
            return state.player.coins
        else:
            pass
    for each in win:
        if conclusion is each:
            for coin in bet:
                state.player.coins.append(Coin(coin))
            return state.player.coins
        else:
            pass
    return state.player.coins


def coin_bust(coin_bag, state: GameState):
    if len(coin_bag) is 0:
        coin_bag = state.player.make_coin_bag()
        return coin_bag
    else:
        return coin_bag
