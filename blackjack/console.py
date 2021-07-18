from core import (
    GameState, render_hand, render_dealer, Conclusion, hand_total, parse_play, Play, make_deck,
    initial_deal, has_blackjack, hit, get_winner, check_deck, set_table,
    check_split, split_hand, Player, Dealer, card_point, check_blackjack_or_bust, check_for_bust
    )

import random


def show_cards(state: GameState):
    for hands in state.player.hands:
        print(f'\nPlayer 1: {render_hand(hands.cards)}')
    print(f'The House: {render_dealer(state.dealer.hand)}\n')
    return


def display_winner(conclusion: Conclusion, state: GameState, hand):
    player_total = hand_total(hand.cards)
    house_total = hand_total(state.dealer.hand.cards)
    if conclusion is Conclusion.Push:
        print("")
        print(f'The House: {render_hand(state.dealer.hand.cards)}= {house_total}')
        print(f'Player 1: {render_hand(hand.cards)}= {player_total} \n PUSH!')
        print("")
        return
    if conclusion is Conclusion.PlayerBj:
        print("")
        print(f'The House: {render_hand(state.dealer.hand.cards)}= {house_total}')
        print(f'BLACKJACK! {render_hand(hand.cards)}= {player_total} \nYOU WIN!')
        print("")
        return
    if conclusion is Conclusion.HouseBj:
        print("")
        print(f'Player 1: {render_hand(hand.cards)}= {player_total}')
        print(f'BLACKJACK! {render_hand(state.dealer.hand.cards)}= {house_total} \nHouse wins!')
        print("")
        return
    if conclusion is Conclusion.PlayerBust:
        print("")
        print(f'The House: {render_hand(state.dealer.hand.cards)}= {house_total}')
        print(f'You Bust! {render_hand(hand.cards)}= {player_total} \nHouse Wins!')
        print("")
        return
    if conclusion is Conclusion.HouseBust:
        print("")
        print(f'Player 1: {render_hand(hand.cards)}= {player_total}')
        print(f'House Busts: {render_hand(state.dealer.hand.cards)}= {house_total} \nYou Win!')
        print("")
        return
    if conclusion is Conclusion.HouseWin:
        print("")
        print(f'The House: {render_hand(state.dealer.hand.cards)}= {house_total}')
        print(f'Player 1: {render_hand(hand.cards)}= {player_total} \n House Wins!')
        print("")
        return
    if conclusion is Conclusion.PlayerWin:
        print("")
        print(f'The House: {render_hand(state.dealer.hand.cards)}= {house_total}')
        print(f'Player 1: {render_hand(hand.cards)}= {player_total} \n YOU Win!')
        print("")
        return
    raise ValueError(f'Winner Inconclusive for {conclusion}')


def get_hit_or_stay(hand) -> Play:
    total = hand_total(hand.cards)
    if check_blackjack_or_bust(hand) is Play.Stay:
        return check_blackjack_or_bust(hand)
    while True:
        response = input(f'Player 1: {render_hand(hand.cards)}\n'
                         f'Your Total is {total}.'
                         f' would you like to Hit? ("y" or "n"): ')
        print('')
        play = parse_play(response)
        if play is None:
            print("Please choose 'y' or 'n'.")
            continue
        else:
            return play


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


def split_response(state: GameState):
    while True:
        split = input(f'You have a split opportunity:'
                      f' {render_hand(state.player.active_hand().cards)} '
                      f'({(card_point(state.player.active_hand().cards[0])+card_point(state.player.active_hand().cards[1]))}'
                      f' Points).\n '
                      f'Would you like to split your hand? ("y" or "n"): ')
        if check_split_response(split) is None:
            print('Please Choose "y" or "n"!')
            continue
        else:
            return check_split_response(split)


def check_split_response(split):
    if split == 'y':
        return True
    elif split == 'n':
        return False
    else:
        return None


def blackjack_or_bust_io(hand):
    if has_blackjack(hand):
        print('You Got A Blackjack!\n')
        return None
    if check_for_bust(hand.cards):
        print('BUSTED!\n')
        return None


def hit_loop(state):
    for hand in state.player.hands:
        hit_or_not = get_hit_or_stay(hand)
        hit(hit_or_not, state, hand)
        blackjack_or_bust_io(hand)
        while hit_or_not is Play.Hit:
            hit_or_not = get_hit_or_stay(hand)
            hit(hit_or_not, state, hand)
            if hit_or_not == Play.Hit and hand_total(state.player.active_hand().cards) < 21:
                continue


def initial_assessment(state: GameState):
    if check_blackjack_or_bust(state.player.active_hand()):
        display_winner(get_winner(state, state.player.active_hand()),
                       state, state.player.active_hand())
        if check_play_again():
            set_table(state, check_deck(state))
            return
        else:
            return


def should_split_or_not(state: GameState):
    if check_split(state) and split_response(state):
        split_hand(state)
        show_cards(state)
        return
    else:
        return


def determine_hand_conclusions(state: GameState):
    for hand in state.player.hands:
        winner = get_winner(state, hand)
        display_winner(winner, state, hand)
    return


def main():
    state = GameState(deck=make_deck(), player=Player(), dealer=Dealer())
    random.shuffle(state.deck)
    initial_deal(state)

    while True:
        show_cards(state)
        initial_assessment(state)
        should_split_or_not(state)
        hit_loop(state)
        determine_hand_conclusions(state)
        if check_play_again() is True:
            set_table(state, check_deck(state))
            continue
        else:
            break


if __name__ == "__main__":
    main()
