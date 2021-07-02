from core import (
    GameState, render_hand, render_dealer, Conclusion, hand_total, parse_play, Play, make_deck,
    initial_deal, has_blackjack, hit, get_winner, check_deck, check_split_response,
    set_table, split_hand, check_split, best_hand, check_for_bust
    )

# TODO DELETE LATER
from core import Card, Rank, Suit

import random


def show_cards(state: GameState):
    print("")
    print(f'Player 1: {render_hand(state.player)}')
    print(f'The House: {render_dealer(state.dealer_hand)}\n')
    return


def display_winner(conclusion: Conclusion, state: GameState):
    player_total = hand_total(state.player)
    house_total = hand_total(state.dealer_hand)
    if conclusion is Conclusion.Push:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player)}= {player_total} \n PUSH!')
        print("")
        return
    if conclusion is Conclusion.PlayerBj:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'BLACKJACK! {render_hand(state.player)}= {player_total} \nYOU WIN!')
        print("")
        return
    if conclusion is Conclusion.HouseBj:
        print("")
        print(f'Player 1: {render_hand(state.player)}= {player_total}')
        print(f'BLACKJACK! {render_hand(state.dealer_hand)}= {house_total} \nHouse wins!')
        print("")
        return
    if conclusion is Conclusion.PlayerBust:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'You Bust! {render_hand(state.player)}= {player_total} \nHouse Wins!')
        print("")
        return
    if conclusion is Conclusion.HouseBust:
        print("")
        print(f'Player 1: {render_hand(state.player)}= {player_total}')
        print(f'House Busts: {render_hand(state.dealer_hand)}= {house_total} \nYou Win!')
        print("")
        return
    if conclusion is Conclusion.HouseWin:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player)}= {player_total} \n House Wins!')
        print("")
        return
    if conclusion is Conclusion.PlayerWin:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player)}= {player_total} \n YOU Win!')
        print("")
        return
    raise ValueError(f'Winner Inconclusive for {conclusion}')


def get_hit_or_stay(hand) -> Play:
    total = hand_total(hand)
    response = input(f'{render_hand(hand)}Your Total is {total}.\n'
                     f' would you like to Hit? ("y" or "n"): ')
    play = parse_play(response)
    if play:
        return play
    else:
        print("Please choose 'y' or 'n'.")


def check_play_again():
    while True:
        a = input("Would you like to play again? ('y' or 'n'): ")
        print("")
        if a == 'y':
            return True
        elif a == 'n':
            print('Goodbye!')
            return False
        else:
            print('Please Choose "y" or "n"!')
            continue


def get_split_response(state, split_check):
    if split_check is True:
        split = input(f'You have a split opportunity:'
                      f' {render_hand(state.player)} ({hand_total(state.player)}Points).\n '
                      f'Would you like to split your hand?: ')
        print(f"\n")
        return check_split_response(split)


def main():
    state = GameState(deck=make_deck(), player=[], hands=[], dealer_hand=[])
    random.shuffle(state.deck)
    initial_deal(state)

    # TODO DELETE LATER
    state.player = [Card(Rank.King, Suit.Clubs), Card(Rank.King, Suit.Spades)]

    while True:
        show_cards(state)
        state.hands = split_hand(get_split_response(state, check_split(state)), state)
        state.player = state.hands

        if len([state.hands]) > 1:
            for each in state.hands:
                if has_blackjack(each):
                    print(f'YOU GOT A BLACKJACK!')
                    if check_play_again() is True:
                        set_table(state, check_deck(state))
                        continue
                    else:
                        break

        for hand in state.hands:
            print(f'{render_hand(hand)}')

        loop = True
        while loop:
            for hand in state.hands:
                hit_or_not = get_hit_or_stay(hand)
                hit(hit_or_not, hand, state)
                if hit_or_not == Play.Hit:
                    loop = True
                    continue
                else:
                    loop = False

        state.player = best_hand(state)
        winner = get_winner(state)
        display_winner(winner, state)

        if check_play_again() is True:
            set_table(state, check_deck(state))
            continue
        else:
            break


if __name__ == "__main__":
    main()
