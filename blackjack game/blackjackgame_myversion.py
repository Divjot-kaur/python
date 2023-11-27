############### Blackjack Project #####################
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
from art import logo
import random
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return(random.choice(cards))

def game_play():
    print(logo)
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0 

    user_cards.append(deal_card()) 
    user_cards.append(deal_card()) 
    user_score = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    computer_cards.append(deal_card())
    computer_score = computer_cards[0]
    print(f"Computer's first card: {computer_cards[0]}")

    cards_continue = True
    while cards_continue:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == 'y':
             user_cards.append(deal_card())
             user_score += user_cards[-1]
             if user_score > 21 and 11 in user_cards:
                 user_cards.remove(11)
                 user_cards.append(1)
                 user_score = sum(user_cards)
             print(f"Your cards: {user_cards}, current score: {user_score}")
             print(f"Computer's first card: {computer_cards[0]}")
        if another_card == 'n' or user_score > 21:
            cards_continue = False
            print(f"Your final hand: {user_cards}, final score: {user_score}")
            computer_cards.append(deal_card())
            computer_score += computer_cards[-1]
            while computer_score < 17:
                computer_cards.append(deal_card())
                computer_score += computer_cards[-1]
            if computer_score > 21 and 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
                computer_score = sum(computer_cards)
            print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
            if user_score > 21:
                print("You went over. You lose!!!")
            elif computer_score > 21:
                print("You win! computer went over.")
            elif user_score > computer_score:
                print("You win")
            elif user_score < computer_score:
                print("Computer wins! You lose")
            else: 
                print("its a draw")

game_continue = True
while game_continue:
    is_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if is_play == "y":
        game_play()
    else:
        game_continue = False
