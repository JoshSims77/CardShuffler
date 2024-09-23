# lib\src\engine\utils.py

#Different shuffling algorithims live here. "Perfect" functions are mainly used in testing. 
import random

from lib.src.engine.deck import Deck

class Shuffle:

    def __init__(self, deck):
        self.deck = deck  # Store passed in cards

    #The Master Shuffle. This is all that needs to be called for a complete randomization. 
    def Shuffle(self):

        for i in range(8):
            # Split the deck based on the random wheel
            first_half, second_half = self.Split()

            # Determine if the split was perfect or imperfect
            if len(first_half) == len(second_half):
                # Call perfect shuffles
                self.Perfect_Shuffles(first_half, second_half)
            else:
                # Call imperfect shuffles
                self.Imperfect_Shuffles(first_half, second_half)




    #Splits

    # Spin the split wheel! 
    def Split(self):
        Wheel = random.random()  # Get a random float between 0.0 and 1.0
        print("Wheel: " + str(Wheel))
        if 0 < Wheel < 0.33:
            print("Perfect Split! 33%")
            return self.Perfect_Split_Deck()  # 33% chance
        elif 0.34 <= Wheel <= 0.54:
            print("Right Hand Split! 20%")
            return self.Right_Hand_Split_Deck()  # 20% chance
        elif 0.55 <= Wheel <= 0.75:
            print("Left Hand Split! 20%")
            return self.Left_Hand_Split_Deck()  # 20% chance
        elif 0.76 <= Wheel <= 0.87:
            print("Heavy Right Hand Split! 11%")
            return self.Heavy_Right_Hand_Split_Deck()  # 11% chance
        elif 0.88 <= Wheel <= 0.99:
            print("Heavy Left Hand Split! 11%")
            return self.Heavy_Left_Hand_Split_Deck()  # 11% chance
        else:
            print("Wild Split! 5%")
            return self.Wild_Split_Deck()  # 5% chance

    # Helper functions for various shuffles, splits deck into two halves. (33% chance)
    def Perfect_Split_Deck(self):
        half = len(self.deck.cards) // 2
        first_half = self.deck.cards[:half]
        second_half = self.deck.cards[half:]
        return first_half, second_half

    # One extra card in first half (right hand) (20% chance)
    def Right_Hand_Split_Deck(self):
        first_half, second_half = self.Perfect_Split_Deck()  # Call Perfect Split first
        card_to_move = second_half.pop(0)
        first_half.append(card_to_move)
        return first_half, second_half

    # One extra card in second half (left hand) (20% chance)
    def Left_Hand_Split_Deck(self):
        first_half, second_half = self.Perfect_Split_Deck()  # Call Perfect Split first
        card_to_move = first_half.pop(0)  # Remove the first card from first_half
        second_half.append(card_to_move)  # Append it to second_half
        return first_half, second_half

    # Two extra cards in first half (right hand) (11% chance)
    def Heavy_Right_Hand_Split_Deck(self):
        first_half, second_half = self.Perfect_Split_Deck()  # Call Perfect Split first
        for _ in range(2):  # Move two cards
            if second_half:  # Check if there are cards to move
                card_to_move = second_half.pop(0)
                first_half.append(card_to_move)
        return first_half, second_half

    # Two extra cards in second half (left hand) (11% chance)
    def Heavy_Left_Hand_Split_Deck(self):
        first_half, second_half = self.Perfect_Split_Deck()  # Call Perfect Split first
        for _ in range(2):  # Move two cards
            if first_half:  # Check if there are cards to move
                card_to_move = first_half.pop(0)
                second_half.append(card_to_move)
        return first_half, second_half

    # 3 to 5 extra cards in either hand (5% chance)
    def Wild_Split_Deck(self): 
        first_half, second_half = self.Perfect_Split_Deck()  # Call Perfect Split first
        extra_cards = random.randint(3, 5)  # Generate a random number of extra cards between 3 and 5
        direction = random.randint(0, 1)  # 0 for right hand, 1 for left hand

        for _ in range(extra_cards):
            if direction == 0 and second_half:  # If moving to right hand and there are cards in second_half
                card_to_move = second_half.pop(0)
                first_half.append(card_to_move)
            elif direction == 1 and first_half:  # If moving to left hand and there are cards in first_half
                card_to_move = first_half.pop(0)
                second_half.append(card_to_move)

        return first_half, second_half


    def Perfect_Shuffles(self, first_half, second_half):
        pathway = random.randint(0,1)
        if pathway == 1:
            self.In_Perfect_Riffle_Shuffle(first_half, second_half)
        else:
            self.Out_Perfect_Riffle_Shuffle(first_half, second_half)
            
    def Imperfect_Shuffles(self, first_half, second_half):
        pathway = random.randint(0,1)
        if pathway == 1:
            self.In_Imperfect_Riffle_Shuffle(first_half, second_half)
        else:
            self.Out_Imperfect_Riffle_Shuffle(first_half, second_half)



    #Riffle Shuffles
    def In_Perfect_Riffle_Shuffle(self, first_half, second_half):
       

        shuffled_deck = []

        # Interleave starting with the second half (left hand), then the first half (right hand) This is called a perfect in riffle shuffle.
        print("In Perfect Riffle!")
        print(f"First Half: {len(first_half)}")
        print(f"Second Half: {len(second_half)}")
        assert len(first_half) == len(second_half), "Perfect riffle shuffle requires even halves."
        for left_card, right_card in zip(second_half, first_half):
            shuffled_deck.append(left_card)  # Add from left hand (second half)
            shuffled_deck.append(right_card) # Add from right hand (first half)

        # Update the deck with the shuffled cards
        self.deck.cards = shuffled_deck

    def Out_Perfect_Riffle_Shuffle(self, first_half, second_half):
        

        shuffled_deck = []

        # Interleave starting with the first half (right hand), then the second half (left hand) This is called a perfect out riffle shuffle.
        print("Out Perfect Riffle!")
        print(f"First Half: {len(first_half)}")
        print(f"Second Half: {len(second_half)}")
        assert len(first_half) == len(second_half), "Perfect riffle shuffle requires even halves."

        for right_card, left_card in zip(first_half, second_half):
            shuffled_deck.append(right_card) # Add from right hand (first half)
            shuffled_deck.append(left_card)  # Add from left hand (second half)

        # Update the deck with the shuffled cards
        self.deck.cards = shuffled_deck
            

    def In_Imperfect_Riffle_Shuffle(self, first_half, second_half):
        shuffled_deck = []

        # Interleave starting with the second half (left hand), then the first half (right hand). This is called an in imperfect riffle shuffle
        print("In Imperfect Riffle!")
        print(f"First Half: {len(first_half)}")
        print(f"Second Half: {len(second_half)}")
        while first_half and second_half:
            shuffled_deck.append(second_half.pop(0))  # Add from left hand (second_half)
            shuffled_deck.append(first_half.pop(0))  # Add from right hand (first_half)

        # If any cards remain in first_half or second_half, add them to the top of the shuffled cards.
        shuffled_deck.extend(second_half)  
        shuffled_deck.extend(first_half) 

        # Update the deck with the shuffled cards
        self.deck.cards = shuffled_deck
    

    def Out_Imperfect_Riffle_Shuffle(self, first_half, second_half):
        shuffled_deck = []

        # Interleave starting with the first half (right hand), then the second half (left hand) this is called an out imperfect riffle shuffle
        print("Out Imperfect Riffle!")
        print(f"First Half: {len(first_half)}")
        print(f"Second Half: {len(second_half)}")
        while first_half and second_half:
            shuffled_deck.append(first_half.pop(0))  # Add from right hand (first_half)
            shuffled_deck.append(second_half.pop(0))  # Add from left hand (second_half)

        # If any cards remain in first_half or second_half, add them to the top of the shuffled cards.
        shuffled_deck.extend(first_half) 
        shuffled_deck.extend(second_half) 

        # Update the deck with the shuffled cards
        self.deck.cards = shuffled_deck
    
