from blackjack import Card, Suit, Rank, card_point, retotal

A = Card(Rank.Ace, Suit.Spades)
r2 = Card(Rank.Two, Suit.Spades)
r3 = Card(Rank.Three, Suit.Spades)
r4 = Card(Rank.Four, Suit.Spades)
r5 = Card(Rank.Five, Suit.Spades)
r6 = Card(Rank.Six, Suit.Spades)
r7 = Card(Rank.Seven, Suit.Spades)
r8 = Card(Rank.Eight, Suit.Spades)
r9 = Card(Rank.Nine, Suit.Spades)
r10 = Card(Rank.Ten, Suit.Spades)
J = Card(Rank.Jack, Suit.Spades)
Q = Card(Rank.Queen, Suit.Spades)
K = Card(Rank.King, Suit.Spades)


def test_card_point():
    assert card_point(Card(Rank.Ace, Suit.Spades)) == 11
    assert card_point(Card(Rank.Five, Suit.Diamonds)) == 5
    assert card_point(Card(Rank.King, Suit.Hearts)) == 10
    assert card_point(Card(Rank.Jack, Suit.Clubs)) == 10


def test_retotal():
    assert retotal([A, r9, r3]) == 13
    assert retotal([A, A]) == 12
    assert retotal([A, r2, r4, A, r4]) == 12
    assert retotal([A, r5, r6]) == 12
    assert retotal([J, A]) == 21
    assert retotal ([K, K, A]) == 21
    assert retotal([A, A, r3]) == 15
    assert retotal([A, A, A, A, A, A, A, A, A, A, A, A]) == 12
    assert retotal([A, A, A, A, A, A, A, A, A, A, A]) == 21
