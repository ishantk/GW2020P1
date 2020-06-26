# We can specify input names during our execution of function for no confused
def register_user(name="", phone="", email="", otp=1234):
    print("Phone:", phone, "OTP:", otp)
    print("Thank you for registering with us", name, email)


name = input("Enter Your Name:")
register_user(name=name, otp=3027)