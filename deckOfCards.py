from random import shuffle


class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:

    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6",
                      "7", "8", "9", "10", "J", "Q", "K"]
        # Creating 52 card objects using Card class
        self.cards = [Card(x, y)for x in suits for y in values]

    # Count how many objects are in Deck class
    def count(self):
        return len(self.cards)

    # Representation of number in Deck class.
    # Here we are calling count object method
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    # Here is hearth of dealing cards logic.
    # This method is private and only used inside class
    def _deal(self, number):
        global dealt_cards

        try:
            # Logic for deal_card method
            if number == 1:
                return self.cards.pop()

            # Logic for deal_hand method
            else:
                counter = number
                dealt_cards = []
                while counter > 0:
                    dealt_cards.append(self.cards.pop())
                    counter -= 1
                return dealt_cards

        # Inform we want to deal more cards than are left in Deck
        except IndexError:
            print("All cards have been dealt")
            return dealt_cards

    # Method that shuffle our deck.
    # Return ValueError if deck don't have 52 cards.
    def shuffle(self):
        if self.count() == 52:
            return shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")

    # Method to deal one card.
    def deal_card(self):
        return self._deal(1)

    # Method to deal how many cards we want
    def deal_hand(self, number):
        return self._deal(number)


my_deck = Deck()             # Creating Deck (list of 52 card objects)
print(my_deck)               # Return representation of new created Deck
my_deck.shuffle()            # Shuffle our full Deck (52 card objects)
card = my_deck.deal_card()   # Deal one card from Deck
print(card)                  # Return dealt card
hand = my_deck.deal_hand(5)  # Deal five cards from Deck
print(hand)                  # Return dealt cards
print(my_deck)               # Return representation of modified Deck
