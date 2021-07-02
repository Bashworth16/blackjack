from core import (
    GameState, render_hand, render_dealer, Conclusion, hand_total, parse_play, Play, make_deck,
    initial_deal, has_blackjack, hit, get_winner, check_deck, check_split_response,
    set_table
    )

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


def get_hit_or_stay(state: GameState) -> Play:
    total = hand_total(state.player)
    response = input(f'Your Total is {total}.\n'
                     f' would you like to Hit? ("y" or "n"): ')
    play = parse_play(response, state.player, state)
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
                      f' {render_hand(state.player_hand)} ({hand_total(state.player_hand)}Points).\n '
                      f'Would you like to split your hand?: ')
        return check_split_response(split)
    else:
        return False


def main():
    state = GameState(deck=make_deck(), player=[], hands=[], dealer_hand=[])
    random.shuffle(state.deck)
    initial_deal(state)

    while True:
        show_cards(state)
        if has_blackjack(state.player):
            print(f'YOU GOT A BLACKJACK!')
            if check_play_again() is True:
                set_table(state, check_deck(state))
                continue
            else:
                break

        hit_or_not = get_hit_or_stay(state)
        hit(hit_or_not, state)

        if hit_or_not == Play.Hit and hand_total(state.player) < 21:
            continue

        winner = get_winner(state)
        display_winner(winner, state)

        if check_play_again() is True:
            set_table(state, check_deck(state))
            continue
        else:
            break


if __name__ == "__main__":
    main()
