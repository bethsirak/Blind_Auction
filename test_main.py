bidding_list = [{"beth": 20}, {"mat": 120}]

# def cal_winner(bidding_list):
winning_bid = 0
for item in range(len(bidding_list)):
    each_dictionary = bidding_list[item]
    # print(each_dictionary)
    for key in each_dictionary:
        int_values = int(each_dictionary[key])
        if int_values > winning_bid:
            winning_bid = int_values
            winner = key
          
print(f"The winner is {key} with a big of {winning_bid} ")
#print(list(bidding_list[item].keys())[list(bidding_list[item].values()).index(winning_key)])

    # highest_bid = 0
    # values = each_dictionary[values]
    # if values > highest_bid:
    #     values = highest_bid
    #     print(highest_bid)
# print(f"The winner is {key} and the higest bid was {values}")


# print(key, values)
# for key in each_dictionary:
# for key, value in bidding_list[item]:
# # for key in bidding_list[item]:
#     value = bidding_list[item]
#     highest_bid = value
#     if value > highest_bid:
#         value = highest_bid
# print(f"The winner is {name} and the higest bid was {highest_bid}")
# # return

# name is key bid is value
