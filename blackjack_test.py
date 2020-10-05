from blackjack import Card, Suit, Rank, card_point

def test_card_point():
    assert card_point(Card(Rank.Ace, Suit.Spades)) == 11
    assert card_point(Card(Rank.Five, Suit.Diamonds)) == 5
    assert card_point(Card(Rank.King, Suit.Hearts)) == 10
    assert card_point(Card(Rank.Jack, Suit.Clubs)) == 10