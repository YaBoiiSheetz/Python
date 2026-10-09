# Module 3, Problem 2

# The student will enter their last name, midterm and final exam scores (0 – 100 points). Compute
# the total exam points to be the sum of 40% of midterm and 60% of the final exam.
# Display student last name and total exam points.

# inputs: last name, midterm score, final exam score
# process: total exam score = (0.4 * midterm) + (0.6 * final)
# outputs: last name, total exam score

# pseudocode:



# welcome user
# enter last name
# input midterm score (0-100)
# input final exam score (0-100)
# compute total exam score = (0.4 * midterm) + (0.6 * final)
# display last name and total exam score

# Code:

input('Exam Grade Calculator\nPress Enter to Continue...') # Welcome screen

# Collect last name and test scores
last_name = input("Last name: ")
midterm = float(input("Midterm score (0-100): "))
final_exam = float(input("Final exam score (0-100): "))

total_score = (0.4 * midterm) + (0.6 * final_exam) # Math

# Output line
print(f"{last_name}     Total Exam Score: {total_score:.2f}")
input("Press Enter to exit...")