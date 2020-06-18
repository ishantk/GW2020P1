amount = int(input("Enter Amount Value: "))

# Regular if/else
"""
if amount >= 149:
    print("Eligible to Apply Promo Code")
    print("Apply ZOMATO to get 40% Off upto \u20b9100")
else:
    print("Not Eligible to Apply Promo Code")
"""

# Nested if/else | if/else within the if/else
"""
if amount >= 149:
    print("Eligible to Apply Promo Code")
    print("Apply CRAVINGS to get 40% Off Upto \u20b9100")

    promoCode = input("Enter the Promo Code: ")
    if promoCode == "CRAVINGS":
        discount = 0.40 * amount

        if discount >= 100:
            discount = amount - discount

        amountToPay = amount - discount

        print("Discount of \u20b9", discount, "applied. Please Pay: \u20b9", amountToPay)
    else:
        print("Sorry !! Promo Code Not Applicable")
        print("Please Pay: \u20b9", amount)

else:
    print("Not Eligible to Apply Promo Code")
"""


# CRAVINGS: 40% Off upto Rs 100 | amount >=149
# JUMBO:    50% Off upto Rs 200 | amount >=500
# BINGO:    Flat 20% Off        | amount >=100

# Ladder if/else
if amount >= 100:
    promoCode = input("Enter the Promo Code: ")

    if promoCode == "CRAVINGS":
        discount = 0.40 * amount

        if discount >= 100:
            discount = 100

        amountToPay = amount - discount
        print("CRAVINGS Applied")
        print("Discount of \u20b9", discount, "applied. Please Pay: \u20b9", amountToPay)

    elif promoCode == "JUMBO":
        discount = 0.50 * amount

        if discount >= 200:
            discount = 200

        amountToPay = amount - discount
        print("JUMBO Applied")
        print("Discount of \u20b9", discount, "applied. Please Pay: \u20b9", amountToPay)

    elif promoCode == "BINGO":
        discount = 0.20 * amount
        amountToPay = amount - discount
        print("BINGO Applied")
        print("Discount of \u20b9", discount, "applied. Please Pay: \u20b9", amountToPay)

    else:
        print("No Such PromoCode", promoCode)
        print("Please Pay: \u20b9", amount)

else:
    print("No PromoCode Applicable")
    print("Please Pay: \u20b9", amount)

# Assignment: In the same program suggest the
# right promo code to the user if user is getting less discounts as compared to the promo code which he has entered

