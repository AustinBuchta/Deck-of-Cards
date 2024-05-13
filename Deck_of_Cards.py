import random

def number_of_card():
    while True:
        try:
            cards = int(input("How many cards would you like?: "))
            if 1 <= cards <= 52:
                return cards
            else:
                print("Number of cards must be between 1 and 52.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

def deck_of_card():
    print("Card Dealer")
    print("\nI have shuffled a deck of 52 cards.\n")
    # Populate the deck with cards
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = []
    for suit in suits:
        for rank in ranks:
            card = f"{rank} of {suit}"
            deck.append(card)
    random.shuffle(deck)  # Shuffle the deck
    return deck, suits, ranks 

def main():
    deck, suits, ranks = deck_of_card()
    num_cards = number_of_card()

    # Display the selected number of cards
    print("\nHere are your cards:")
    for i in range(num_cards):
        print(deck[i])
        
    # Calculate and display the number of remaining cards
    remaining_cards = len(deck) - num_cards
    print("\nRemaining cards in the deck:", remaining_cards)
    print("\nGood luck!")
if __name__ == "__main__":
    main()