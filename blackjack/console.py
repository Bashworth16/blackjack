from blackjack.core import GameState, render_hand, render_dealer, Conclusion, hand_total, parse_play, Play, make_deck, \
    initial_deal, has_blackjack, hit, get_winner

import random


def show_cards(state: GameState):
    print("")
    print(f'Player 1: {render_hand(state.player_hand)}')
    print(f'The House: {render_dealer(state.dealer_hand)}\n')


def display_winner(winner: Conclusion, state: GameState):
    player_total = hand_total(state.player_hand)
    house_total = hand_total(state.dealer_hand)
    if winner is Conclusion.Push:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n PUSH!')
        print("")
        return
    if winner is Conclusion.PlayerBj:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'BLACKJACK! {render_hand(state.player_hand)}= {player_total} \nYOU WIN!')
        print("")
        return
    if winner is Conclusion.HouseBj:
        print("")
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total}')
        print(f'BLACKJACK! {render_hand(state.dealer_hand)}= {house_total} \nHouse wins!')
        print("")
        return
    if winner is Conclusion.PlayerBust:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'You Bust! {render_hand(state.player_hand)}= {player_total} \nHouse Wins!')
        print("")
        return
    if winner is Conclusion.HouseBust:
        print("")
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total}')
        print(f'House Busts: {render_hand(state.dealer_hand)}= {house_total} \nYou Win!')
        print("")
        return
    if winner is Conclusion.HouseWin:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n House Wins!')
        print("")
        return
    if winner is Conclusion.PlayerWin:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n YOU Win!')
        print("")
        return
    else:
        return 'Winner Inconclusive...'


def get_hit_or_stay(state: GameState) -> Play:
    total = hand_total(state.player_hand)
    s = input(f'Your Total is {total}, would you like to Hit? ("y" or "n"): ')
    play = parse_play(s)
    if play:
        return play
    print("Please choose 'y' or 'n'.")
    return get_hit_or_stay(state)


def play_again():
    while True:
        a = input("Would you like to play again? ('y' or 'n'): ")
        print("")
        if a == 'y':
            return True
        elif a == 'n':
            print('Goodbye!')
            exit()
        else:
            print('Please Choose "y" or "n"!')
            continue


def main():
    state = GameState(deck=make_deck(), player_hand=[], dealer_hand=[])
    random.shuffle(state.deck)
    initial_deal(state)

    while True:
        show_cards(state)
        if has_blackjack(state.player_hand):
            print(f'YOU GOT A BLACKJACK!')
            if play_again() is True:
                state = GameState(deck=make_deck(), player_hand=[], dealer_hand=[])
                random.shuffle(state.deck)
                initial_deal(state)
                continue
            else:
                break

        hit_or_not = get_hit_or_stay(state)
        hit(hit_or_not, state)

        total = hand_total(state.player_hand)

        if hit_or_not == Play.Hit and total < 21:
            continue

        winner = get_winner(state)
        display_winner(winner, state)

        if play_again() is True:
            state = GameState(deck=make_deck(), player_hand=[], dealer_hand=[])
            random.shuffle(state.deck)
            initial_deal(state)
            continue
        else:
            break


if __name__ == "__main__":
    main()
