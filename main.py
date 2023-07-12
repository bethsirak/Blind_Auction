#create dictonary where the name is the key and the bid is the value
#ask user input for name and bid
#add this new name and bid to new dictionary
# after this is added clear the name and bid so it is blind
#ask new user for inputs and repeate steps untill everyone has inputted thier details
#loop through dictonary to find the highest bid and that is the winner

import os
from art import logo 

clear = lambda: os.system("clear")
clear()

print(logo)

def user_bid(name, bid):
    bidders = {}
    bidders[name] = bid
    clear()
    return
    
run_again = True
while run_again:
    print("Welcome to the blind auction")
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    additional_bidders = input("Are there any other bidders? (yes/no)").lower()        
    user_bid(name, bid)
    if additional_bidders == "no":
        run_again = False
   