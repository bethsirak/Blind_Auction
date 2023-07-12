# Blind Auction

Welcome to the Blind Auction! This program allows multiple bidders to participate in an auction anonymously and determines the winner based on the highest bid.

## How to Use

1. When prompted, enter your name as a bidder.
2. Enter your bid amount.
3. Specify whether there are any additional bidders.
4. Repeat steps 1-3 for each bidder.
5. Once all bidders have entered their details, the program will determine the winner.

## Features

- Anonymous bidding: Bidders remain anonymous throughout the auction process.
- Real-time tracking: The program stores each bid and bidder's name for reference.
- Winner determination: The program calculates the highest bid and announces the winner.

## Dependencies

This program requires the following dependencies:

- Python 3.x

## Getting Started

1. Clone this repository to your local machine.
2. Ensure that Python 3.x is installed.
3. Run the program using a Python interpreter: `python blind_auction.py`
4. Follow the on-screen prompts to participate in the auction.
5. Once all bidders have submitted their bids, the winner will be announced.

## Example

Welcome to the Blind Auction!

What is your name? John
What is your bid? 500
Are there any other bidders? (yes/no) yes

What is your name? Jane
What is your bid? 700
Are there any other bidders? (yes/no) no

The winner is Jane with a bid of 700.


## ASCII Art

The program uses ASCII art for visual appeal. The art is stored in a separate file named `art.py`. Make sure to keep this file in the same directory as the program for proper execution.

## Program Complexity

The program utilizes a nested data structure to store the bids. Each bid is stored as a dictionary within a list. This was to test my knowledge and understanding of the different data structures with a higher complexity

Good luck with your bidding!
