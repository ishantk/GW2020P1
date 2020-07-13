print("~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Prize Rewards")
print("~~~~~~~~~~~~~~~~~~~~~~~~")

prize_money = [100, 120, 50, 90, 30]
idx = int(input("Enter Your Lucky Number: "))
try:
    print("For Your Lucky Number, You have Won", prize_money[idx], "CashBack")
except Exception as e:
    print("OOPS!! You may not be lucky !! Message:", e)
finally:    # will be executed at any cost. regardless exception is handled or not
    print("Don't Worry, A Default CashBack of 10 will also be granted :)")

print("Thank You for Your Participation")


# Exception is a built in class
# It can be used to handle any type of Error
# As all the Errors are Children of Exception class in Python
"""
    Some Internal Hierarchy:
    
    class Exception:
        pass
        
    class ZeroDivisionError(Exception):
        pass
        
    class IndexError(Exception):
        pass            

    # Try can work with multiple except cases
    try:
        pass
    except  ZeroDivisionError as e1:
        pass
    except  IndexError as e2:
        pass  
    
    # Rather than multiple except cases, we can use a single except case with Exception i.e. Parent class
    try:
        pass
    except  Exception as e:
        pass     

"""