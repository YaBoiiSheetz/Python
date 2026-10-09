# Enter the make, model, msrp amount and discount percent of an auto you are interested in.
# Compute the amount off msrp you will receive as well as the discounted price. The amount off is
# computed to be the msrp times the discount percent (you can enter as a decimal so no need to
# divide by 100). The discounted price is the msrp minus the amount off. Display the make, model,
# mrsp, discount percent, amount off and discounted price.

# input:
# make, model, MSRP Price, discount percent
# process: 
# money_saved = (MSRP * discount_percent)
# discount_price = (MSRP * (1-discount_percent))
# output: make, model, MSRP, discount percent, money saved, discounted price


# Code


print("Cole's Used Cars Discount Generator")
input("Press Enter to continue...")
vehicle_make = input("Vehicle Make: ")
vehicle_model = input("Vehicle Model: ")
vehicle_msrp = round(float(input("Vehicle MSRP: $")), 2)
discount_percent = (
    round(
        float(
            input(
                "Enter discount percentage as a decimal (example: 25% is .25): "
                )
            )
        , 2)
)

money_saved = round((vehicle_msrp * discount_percent), 2)
discount_price = round((vehicle_msrp * (1 - discount_percent)), 2)

print (
    f"\nThe {vehicle_make} {vehicle_model} usually retails for ${vehicle_msrp:,}"
    f" at MSRP, but with our {int(discount_percent * 100)}% discount at\n"
    f"Cole's Used Cars, you only have to pay ${discount_price:,}, saving you ${money_saved:,}!"
)