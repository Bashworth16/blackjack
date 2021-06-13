import tkinter as tk
import random
from blackjack.core import GameState, hand_total, Play, make_deck, \
    initial_deal, has_blackjack, hit, get_winner


def show_cards(state):
    game_state = tk.Label(text=f"{state.player_hand}")
    game_state.pack()
    return game_state


def display_total(total):
    card_total = tk.Label(text=f"{total}")
    card_total.pack()
    return card_total


def get_hit_or_stay(state):
    no = tk.Button(text="No")
    no.pack()
    return no


def display_winner(winner, state):
    pass


def play_again():
    pass


def main():
    window = tk.Tk()
    window.mainloop()
    state = GameState(deck=make_deck(), player_hand=[], dealer_hand=[])
    random.shuffle(state.deck)
    initial_deal(state)

    while True:
        show_cards(state)
        display_total(hand_total(state.player_hand))
        if has_blackjack(state.player_hand):
            print(f'YOU GOT A BLACKJACK!')
            break

        hit_or_not = get_hit_or_stay(state)
        hit(hit_or_not, state)

        total = hand_total(state.player_hand)

        if hit_or_not == Play.Hit and total < 21:
            continue

        winner = get_winner(state)
        display_winner(winner, state)

        if winner:
            break

    play_again()


if __name__ == "__main__":
    main()
