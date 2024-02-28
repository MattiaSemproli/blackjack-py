from Hand import *
from Deck import *

"""
BlackjackGame class

This class represents a game of Blackjack. It has methods to deal initial cards, handle the player's turn, dealer's turn, and determine the winner.
"""
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

    def deal_initial_cards(self):
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())
        self.player_hand.add_card(self.deck.draw())
        self.dealer_hand.add_card(self.deck.draw())

    def player_turn(self):
        while True:
            print("Your hand:")
            for card in self.player_hand.cards:
                print(f"    -> [{card}]")
            print(f"Total value: {self.player_hand.get_value()}")

            print("\n---------------------\n")

            print("Dealer hand:")
            for i, card in enumerate(self.dealer_hand.cards):
                if i == 0:
                    print("    -> [Hidden card]")
                else:
                    print(f"    -> [{card}]")
            print(f"Total value: {self.dealer_hand.get_dealer_value_with_hidden_card()}")

            choice = input("\nDo you want to hit or stand? (h/s): ").lower()
            if choice == 'h':
                hit = self.deck.draw()
                print(f"\nYou draw: {hit}")
                self.player_hand.add_card(hit)
                tot = self.player_hand.get_value()
                if tot > 21:
                    print(f"Total value: {tot} > 21, That's bust! You lose.")
                    return
            else:
                break

    def dealer_turn(self):
        print("Dealer hand:")
        for card in self.dealer_hand.cards:
            print(f"    -> [{card}]")
        print(f"Total value: {self.dealer_hand.get_value()}")
        while self.dealer_hand.get_value() < 17:
            dealer_hit = self.deck.draw()
            print(f"\nDealer draw: {dealer_hit}")
            self.dealer_hand.add_card(dealer_hit)
            tot = self.dealer_hand.get_value()
            if tot > 21:
                print(f"Total value: {tot} > 21, Dealer bust! You win.")
                return

    def determine_winner(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()

        print(f"\nYour total value: {player_value}")
        print(f"Dealer's total value: {dealer_value}\n")

        if player_value > dealer_value:
            print("You win!")
        elif player_value < dealer_value:
            print("Dealer wins.")
        else:
            print("It's a tie.")

    def run(self):
        print("Welcome to Blackjack!\n")
        game_id = 1
        while True:
            if game_id == 1:
                self.deck = Deck()
            self.player_hand = Hand()
            self.dealer_hand = Hand()
            self.deal_initial_cards()

            self.player_turn()
            if self.player_hand.get_value() <= 21:
                self.dealer_turn()
                if self.dealer_hand.get_value() <= 21:
                    self.determine_winner()

            play_again = input("\nDo you want to play again? (y/n): ").lower()
            if play_again == 'y':
                play_continue = input("\nDo you want to continue or restart? (c/r): ").lower()
                if play_continue == 'c':
                    game_id += 1
                    print(f"Game {game_id} is starting...\n")
                elif play_continue == 'r':
                    game_id = 1
                else:
                    break
            else:
                break