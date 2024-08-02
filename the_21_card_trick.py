
def initialize_deck():
   return list(range(1, 22))

def display_piles(piles):
    for i in range(max(len(pile) for pile in piles)):
        row = ""
        for pile in piles:
            if i < len(pile):
                row += f"{pile[i]:>3} "
            else:
                row += "   "
        print(row)
    print("\n")

def deal_piles(deck):
    piles = [[], [], []]
    for i, card in enumerate(deck):
        piles[i % 3].append(card)
    return piles

def collect_piles(piles, chosen_pile_index):
    chosen_pile = piles[chosen_pile_index]
    other_piles = [piles[i] for i in range(3) if i != chosen_pile_index]
    return other_piles[0] + chosen_pile + other_piles[1]

def card_trick():
    deck = initialize_deck()
    for round in range(3):
        print(f"Round {round + 1}:")
        piles = deal_piles(deck)
        display_piles(piles)

        while True:
            try:
                chosen_pile_index = int(input("Choose the pile (1, 2, or 3) where your card is: ")) - 1
                if 0 <= chosen_pile_index < 3:
                    break
                else:
                    print("Invalid choice. Please choose 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        deck = collect_piles(piles, chosen_pile_index)

    print(f"Your card is the {deck[10]}-th card in the final deck!")

card_trick()
