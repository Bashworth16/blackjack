from core import (
    GameState, render_hand, render_dealer, Conclusion, hand_total, parse_play, Play, make_deck,
    initial_deal, has_blackjack, hit, get_winner, check_deck, check_split_response,
    set_table, check_split, split_hand
)
import random


def show_cards(state: GameState):
    print("")
    print(f'Player 1: {render_hand(state.player_hand)}')
    print(f'The House: {render_dealer(state.dealer_hand)}\n')
    return


def display_winner(conclusion: Conclusion, state: GameState):
    player_total = hand_total(state.player_hand)
    house_total = hand_total(state.dealer_hand)
    if conclusion is Conclusion.Push:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n PUSH!')
        print("")
        return
    if conclusion is Conclusion.PlayerBj:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'BLACKJACK! {render_hand(state.player_hand)}= {player_total} \nYOU WIN!')
        print("")
        return
    if conclusion is Conclusion.HouseBj:
        print("")
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total}')
        print(f'BLACKJACK! {render_hand(state.dealer_hand)}= {house_total} \nHouse wins!')
        print("")
        return
    if conclusion is Conclusion.PlayerBust:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'You Bust! {render_hand(state.player_hand)}= {player_total} \nHouse Wins!')
        print("")
        return
    if conclusion is Conclusion.HouseBust:
        print("")
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total}')
        print(f'House Busts: {render_hand(state.dealer_hand)}= {house_total} \nYou Win!')
        print("")
        return
    if conclusion is Conclusion.HouseWin:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n House Wins!')
        print("")
        return
    if conclusion is Conclusion.PlayerWin:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n YOU Win!')
        print("")
        return
    raise ValueError(f'Winner Inconclusive for {conclusion}')


def get_hit_or_stay(state: GameState) -> Play:
    total = hand_total(state.player_hand)
    response = input(f'Your Total is {total}.\n'
                     f' would you like to Hit? ("y" or "n"): ')
    play = parse_play(response, state.player_hand, state)
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


def get_split_response(state):
    split_response = input(f'You have a split opportunity:'
                           f' {render_hand(state.player_hand)} ({hand_total(state.player_hand)}Points).\n '
                           f'Would you like to split your hand? ("y" or "n"): ')
    return split_response


def main():
    state = GameState(deck=make_deck(), player_hand=[], player_split=[], dealer_hand=[])
    random.shuffle(state.deck)
    initial_deal(state)

    while True:
        show_cards(state)
        if check_split(state) is True:
            split_response = get_split_response(state)
            if check_split_response(split_response) is True:
                split_hand(state)
            else:
                pass
        else:
            pass
        if has_blackjack(state.player_hand):
            print(f'YOU GOT A BLACKJACK!')
            if check_play_again() is True:
                set_table(state, check_deck(state))
                continue
            else:
                break

        hit_or_not = get_hit_or_stay(state)
        hit(hit_or_not, state)

        if hit_or_not == Play.Hit and hand_total(state.player_hand) < 21:
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
