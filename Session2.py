# 1. Storage Container Creation Statement
johnsAge = 20

# johnsAge is a Reference Variable
# It holds HashCode for the Data 20

# 2. Container Read Statement
print("Johns Age is:", johnsAge)
print("Johns Age HashCode is:", id(johnsAge))

jenniesAge = 20
print("Jennies Age is:", jenniesAge)
print("Jennies Age HashCode is:", id(jenniesAge))

print("===================")

# 3. Container Updation Statement
johnsAge = 22

print("Johns Age Now is:", johnsAge)
print("Johns Age HashCode Now is:", id(johnsAge))

print("Jennies Age Now is:", jenniesAge)
print("Jennies Age HashCode Now is:", id(jenniesAge))

# 4. Container Copy Statement | Reference Copy
siasAge = jenniesAge
print("===================")

print("Sias Age is:", siasAge)
print("Sias Age HashCode is:", id(siasAge))

# 5. Container Delete Statement
del jenniesAge

# print("jenniesAge is:", jenniesAge) # if we get error here, nothing below will execute
print("SiasAge is:", siasAge)

# PS: if we delete the variable it will delete everything
#     But, if some other variable also refers to the same data location, it will not delete the data

# REFERENCE VARIABLE : Which Holds the HashCode
print("Sias Age HashCode in Binary is:", bin(id(siasAge)))
print("Sias Age HashCode in Octal is:", oct(id(siasAge)))
print("Sias Age HashCode in Decimal is:", id(siasAge))
print("Sias Age HashCode in Hexa Decimal is:", hex(id(siasAge)))

"""
                                          Base 2 Base 10 Base 8    Base 16
	Assignment: Explore Number Systems -> Binary Decimal Octal and Hexadecimal
												 199
												 1*10pow2 + 9*10pow1 + 9*10pow0	
												 100      +  90		 + 9


"""


