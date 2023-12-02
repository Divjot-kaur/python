from game_data import data
from art import logo, vs 
import random
#from replit import clear

score = 0
print(logo)

def choose_random_index():
    '''choose a random index from the list'''
    return random.randint(0, len(data) - 1)

def compare_followers(count_a, count_b):
    '''comparing folower counts of a and b'''
    if count_a > count_b:
        return "a"
    else:
        return "b"

def increase_score():
    '''increment score by 1'''
    global score
    score += 1
    return score

def game(a,b):
    '''higher or lower game'''
    while a == b:
        b = choose_random_index()
    print(f"Compare A: {data[a]['name']}, {data[a]['description']}, from {data[a]['country']}")
    print(vs)
    print(f"Compare B: {data[b]['name']}, {data[b]['description']}, from {data[b]['country']}")
    follower_count_a = data[a]['follower_count']
    follower_count_b = data[b]['follower_count']
    #print(f"a = {follower_count_a}, b = {follower_count_b}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if user_choice == compare_followers(follower_count_a, follower_count_b):
        a = b
        b = choose_random_index()
        increase_score()
        #clear()
        print(logo)
        print(f"You're right! Current score: {score}.")
        game(a,b)
    else: 
        #clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")

game(choose_random_index(), choose_random_index())