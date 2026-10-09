# Module 3, Problem 3

# You and two friends completed a job and received an amount that is entered into the problem.
# You are to split the amount received evenly between the three of you. Compute and display
# what each of you will receive.

# inputs: you and your friends names, amount of money earned
# process: individual share = (amount of money earned / 3)
# output: your share, friend 2's share, and friend 3's share

# Pseudocode:

# Welcome screen
# money earned = input (how much did you and your two friends earn?)
# individual_share = round((money earned / 3), 2 decimal places)
# print("You earned ${individual_share}
# Friend 2 earned ${individual_share}
# Friend 3 earned ${individual_share}")

#Code

input("Payment Splitter\nPress Enter to continue...")
total_pay = float(input("What was the total payment for the job? $"))
ind_pay = round((total_pay / 3), 2)
print(f"Your pay is: ${ind_pay}\nPayment for Friend 1 is: ${ind_pay}\nPayment for Friend 2 is: ${ind_pay}")
input("Press Enter to exit...")
