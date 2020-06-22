# Function Execution Stack
# Whenever we execute function, in the background stack operations comes in action

def computeTaxes(amount):
    taxes = 0.18 * amount
    total = amount + taxes
    return total

# Slope of Line: y = mx + c
def slopeOfLine(m, x, c):
    y = m*x + c
    return y


# execute the functions
print("Taxes for amount 2310 is:", computeTaxes(2310))
print("y is :", slopeOfLine(5, 2, 2))

