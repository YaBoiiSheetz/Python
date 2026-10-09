# Anthony Mazzarisi     M3P1.py     10/08/2026

#  Allow the user to enter the stock ticker symbol (ie MSFT for Microsoft), number of shares and cost per share. 
#  Compute and display amount invested to be number of shares times cost per share

# inputs: Stock Ticker symbol, # of shares, cost per share
# process: # of shares * cost per share = amount invested
# output: ticker symbol, amount invested

# Pseudocode:

# give user a warm welcome
# declare stock ticker symbol as input
# declare cost per share as input
# declare number of shares owned as input
# declare amount invested as (number of shares) * (cost per share)
# output dollar amount invested in declared stock

# Code:

# "\x1b<number>m" is an escape sequence used to color and format strings of text.
# the number in <number> determines the formatting applied.
# "32" makes the text green.
# "4" underlines the text.
# "0" resets the text to default.
# "\n" is the escape sequence to enter a line break.

# Welcome text
input('\x1b[32mStock Investment Calculator\nPress Enter to Continue...\x1b[0m')

# collect information from user
ticker_symbol = input('Enter stock ticker symbol: \x1b[32m').upper() # this string will immediately be converted to UPPERCASE
cost_per_share = float(input('\x1b[0mEnter current cost per share: \x1b[32m$'))
shares_owned = float(input('\x1b[0mEnter number of shares owned: \x1b[32m'))

# boring math
investment_total = (shares_owned * cost_per_share)

#output
print(f"\x1b[0myou have \x1b[4m${investment_total:,.2f}\x1b[0m invested in \x1b[4m{ticker_symbol}\x1b[0m.")

# This final line of code holds the terminal open until the user has read the output and is ready to exit.
# Without it, the program would print the output and immediately close the terminal before the user could read the output.
input("Press enter to exit...")