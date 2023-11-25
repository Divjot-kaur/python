from replit import clear
from art import logo 
#HINT: You can call clear() to clear the output in the console.
print(logo)
def highest_bid(biddings):
    #print(biddings)
    highest = 0 
    winner = ""
    for keys in biddings:
        if biddings[keys] > highest:
            highest = biddings[keys]
            winner = keys
    print(f"the winner is {winner} with a bid of ${highest}")

print("welome to the secret auction program.")
bid_continue = True
bids = {}
while bid_continue:
    name = input("What is your name?: ")
    bid_amount = int(input("what's your bid?: $"))

    bids[name] = bid_amount
    #print(bids)
    
    result = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if result == 'no':
        bid_continue = False
        clear()
        highest_bid(bids)
    else:
        clear()
