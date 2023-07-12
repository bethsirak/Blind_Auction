#create a listing storing dictonaries where the name is the key and the bid is the value
#ask user input for name and bid
#add this new name and bid to new dictionary
# after this is added clear the name and bid so it is blind
#ask new user for inputs and repeat steps untill everyone has inputted thier details
#loop through dictonary to find the highest bid and that is the winner

import os
from art import logo 

clear = lambda: os.system("clear")
clear()

print(logo)

bidding_list = []

def user_bid_dictionary(name, bid):
    bidders = {}
    bidders[name] = bid
    bidding_list.append(bidders)
    clear()
    print(bidding_list)

# def cal_winner(bidding_list):
#     for dictionary in bidding_list:
#         for bid_value in dictionary[name]:
#          highest_bid = dictionary[name]
#          if bid_value > highest_bid:
#             bid_value = highest_bid
#         print(f"The winner is {name} and the higest bid was {highest_bid}")
#     return

    
run_again = True
while run_again:
    print("Welcome to the blind auction")
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    additional_bidders = input("Are there any other bidders? (yes/no)").lower()        
    user_bid_dictionary(name, bid)
    if additional_bidders == "no":
        run_again = False
        # cal_winner(bidding_list)
        # print(cal_winner(bidders))
   