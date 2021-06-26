from core import (
    GameState, render_hand, render_dealer, Conclusion, hand_total, parse_play, Play, make_deck,
    initial_deal, has_blackjack, hit, get_winner, check_split, check_deck, check_split_response,
    split_hand, set_table, check_for_bust
    )

import random


def show_cards(state: GameState):
    print("")
    print(f'Player 1: {render_hand(state.player_hand)}')
    print(f'The House: {render_dealer(state.dealer_hand)}\n')
    return


def display_winner(conslusion: Conclusion, state: GameState):
    player_total = hand_total(state.player_hand)
    house_total = hand_total(state.dealer_hand)
    if conslusion is Conclusion.Push:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n PUSH!')
        print("")
        return
    if conslusion is Conclusion.PlayerBj:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'BLACKJACK! {render_hand(state.player_hand)}= {player_total} \nYOU WIN!')
        print("")
        return
    if conslusion is Conclusion.HouseBj:
        print("")
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total}')
        print(f'BLACKJACK! {render_hand(state.dealer_hand)}= {house_total} \nHouse wins!')
        print("")
        return
    if conslusion is Conclusion.PlayerBust:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'You Bust! {render_hand(state.player_hand)}= {player_total} \nHouse Wins!')
        print("")
        return
    if conslusion is Conclusion.HouseBust:
        print("")
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total}')
        print(f'House Busts: {render_hand(state.dealer_hand)}= {house_total} \nYou Win!')
        print("")
        return
    if conslusion is Conclusion.HouseWin:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n House Wins!')
        print("")
        return
    if conslusion is Conclusion.PlayerWin:
        print("")
        print(f'The House: {render_hand(state.dealer_hand)}= {house_total}')
        print(f'Player 1: {render_hand(state.player_hand)}= {player_total} \n YOU Win!')
        print("")
        return
    raise ValueError(f'Winner Inconclusive for {conslusion}')


def get_hit_or_stay(state: GameState) -> Play:
    if len(state.nested_hands) > 1:
        available_hits = len(state.nested_hands)
        while True:
            for hand in state.nested_hands:
                total = hand_total(hand)
                response = input(f'Your Total for this hand {render_hand(hand)}= {total}.\n'
                                 f' would you like to Hit? ("y" or "n"): ')
                if response is 'y' or 'n':
                    available_hits -= 1
                    play = parse_play(response, hand, state)
                    if available_hits == 1:
                        continue
                    if available_hits == 0:
                        if play:
                            return play
                else:
                    print("Please choose 'y' or 'n'...")
                    continue
    if len(state.nested_hands) == 1:
        total = hand_total(state.player_hand)
        response = input(f'Your Total for this hand {render_hand(state.player_hand)}= {total}.\n'
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


def get_split_response(state, split_check):
    if split_check is True:
        split = input(f'You have a split opportunity:'
                      f' {render_hand(state.player_hand)} ({hand_total(state.player_hand)}Points).\n '
                      f'Would you like to split your hand?: ')
        return check_split_response(split)
    else:
        return False


def main():
    state = GameState(deck=make_deck(), player_split=[], player_hand=[], nested_hands=[], dealer_hand=[])
    random.shuffle(state.deck)
    initial_deal(state)
    state.nested_hands = [state.player_hand]

    while True:
        show_cards(state)
        if has_blackjack(state.player_hand):
            print(f'YOU GOT A BLACKJACK!')
            if check_play_again() is True:
                set_table(state, check_deck(state))
                continue
            else:
                break

        split_hand(get_split_response(state, check_split(state)), state)
        hit_or_not = get_hit_or_stay(state)
        hit(hit_or_not, state)
        check_for_bust(state.player_hand)

        if hit_or_not == Play.Hit:
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
