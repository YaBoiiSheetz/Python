# # Anthony Mazzarisi     M3P5.py     10/9/2026

# Allow the user to enter a radius of a circle. Compute and display the area to be pi times radius
# squared (use 3.14 for pi and multiple radius time radius for radius squared). Also, compute and
# display the perimeter (2 times pi * radius).

# input:
# PI (constant), radius
# process:
# area = (PI * (radius ** 2))
# circumference = (2 * PI * radius)
# output:
# area, circumference

# Code:

PI = 3.14

print("Circle Area/ Circumference Calculator")
input("Press Enter to continue...")
radius = float(input("radius = "))

calc_area = (PI * (radius ** 2))
calc_circumference = (2 * PI * radius)

print(f"area = {calc_area:.2f} units^2")
print(f"circumference = {calc_circumference:.2f} units")