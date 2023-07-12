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

This program utilizes the following external libraries:

- `os`: Provides a way to clear the terminal screen.
- `art`: Enables the display of ASCII art (logo).

Please make sure these dependencies are installed before running the program.

## Getting Started

1. Clone this repository to your local machine.
2. Ensure that the required dependencies are installed.
3. Run the program using a Python interpreter.
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


## Program Complexity

The program utilizes a nested data structure to store the bids. Each bid is stored as a dictionary within a list. This allows for efficient tracking and retrieval of bidder information.

## Additional Notes

- The program uses the `clear` function from the `os` library to provide a clean and user-friendly interface.
- The `art` library is used to display an attractive logo at the beginning of the program.

Good luck with your bidding!

