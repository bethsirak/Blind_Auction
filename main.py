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
    return

def cal_winner(bidding_list):
    winning_bid = 0
    for item in range(len(bidding_list)):
        each_dictionary = bidding_list[item]
        # print(each_dictionary)
        for key in each_dictionary:
            int_values = int(each_dictionary[key])
            if int_values > winning_bid:
                winning_bid = int_values
                winner = key

    print(f"The winner is {winner} with a bid of {winning_bid} ")
    return

    
run_again = True
while run_again:
    print("Welcome to the blind auction")
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    additional_bidders = input("Are there any other bidders? (yes/no)").lower()        
    user_bid_dictionary(name, bid)
    if additional_bidders == "no":
        run_again = False
        cal_winner(bidding_list)
     
   