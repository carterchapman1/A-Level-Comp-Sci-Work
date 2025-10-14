import random
import math

class Card:


    """ A class to describe cards in a pack """
    def __init__(self, number : int):
        self._card_number = number

    def get_suit(self) -> str:
        """ return a string 'C', 'S', 'H', 'D' """
        suits = "SHCD"
        return suits[self._card_number // 13]

    def get_value(self) -> str:
        """ return a string 'A'..'10', 'J', 'Q', 'K' """
        value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        return value[self._card_number % 13]
        

    def get_short_name(self) -> str:
        """ return card name eg '10D' '8C' 'AH' """
        value = card.get_value()
        suit = card.get_suit()
        shortname = value + suit
        return shortname

    def get_long_name(self) -> str:
        """ return card name eg 'Ten of Diamonds' """
        value = ['Ace', '2', '3','4','5','6','7','8','9','10','Jack','Queen','King']
        suit = ['Clubs', "Spades", 'Hearts', 'Diamonds']
        return (value[self._card_number % 13] + ' of ' + suit[self._card_number // 13])


class Deck:
    """ A class to contain a pack of cards with methods for shuffling, adding or removing cards etc. """
    def __init__(self):
        self._card_list = []
        for i in range(52):
            self._card_list.append(Card(i))

    def length(self) -> int:
        """ returns the number of cards still in the deck """
        return len(self._card_list)

    def shuffle_deck(self):
        """ shuffles the cards """
        random.shuffle(self._card_list)

    def take_top_card(self) -> Card:
        """ removes the top card from the deck and returns it (as a card object) """
        card = self._card_list[0]
        self._card_list.remove(card)
        return card

    def add_card(self, new_card):
        """ add a card to the bottom of the deck """
        self._card_list.append(new_card)
        

card = Card(0)
deck = Deck()
deck.shuffle_deck()
for _ in range(deck.length()):
    card = deck.take_top_card()
    print(card.get_long_name())


