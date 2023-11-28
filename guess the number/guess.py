from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!!")
print("I am Thinking of a number between 1 and 100.")
def choose_number():
    '''returns a random number'''
    number = random.randint(1,100)
    return number

def set_difficulty():
    diffuculty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if diffuculty == 'easy':
        return 10
    elif diffuculty == 'hard':
        return 5
    else:
        print("enter the correct value.")
        return 0 

def game():
    random_number = choose_number()
    print(random_number)
    
    attempts_left = set_difficulty()

    while attempts_left > 0:
        print(f"You have {attempts_left} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! the answer was {guess}")
            return
        elif guess < random_number: 
            print("Too Low.")
            attempts_left -= 1
        else:
            print("Too high.")
            attempts_left -= 1
        if attempts_left > 0:
            print("Guess again.")
    print("You've run out of guesses, you lose.")

game()