# THE MAIN FUNCTION
# In our program by default whatever you try to execute belongs to main function

def computeTaxes(amount):           # Creational Statement
    taxes = 0.18 * amount
    total = amount + taxes
    return total

# Slope of Line: y = mx + c
def slopeOfLine(m, x, c):          # Creational Statement
    y = m*x + c
    return y


# Creational Statement: main function in creation
# remember execution begins from main
def main():
    # Execution Statements
    print("Name is:", __name__) # whatever we execute is executed by main. its an entry point in program
    print("Taxes for amount 2310 is:", computeTaxes(2310))
    print("y is :", slopeOfLine(5, 2, 2))
    # when main finishes, program finishes and memory is cleaned up automatically for us

# if as developer we create the main function, we must execute it with a check
if __name__ == "__main__":
    main()
