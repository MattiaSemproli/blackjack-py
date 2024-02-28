"""
Card class

This class represents a playing card. It has a rank and a suit.
"""
class Card:
    heart = "\u2665"
    diamond = "\u2666"
    club = "\u2663"
    spade = "\u2660"

    suits = {
        "Hearts": heart,
        "Diamonds": diamond,
        "Clubs": club,
        "Spades": spade
    }

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = Card.suits[suit]

    def __str__(self):
        return f"{self.rank} of {self.suit}"