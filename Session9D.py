john = {"fionna", "lee", "mike", "kia", "joe", "sia"}
jack = {"dave", "ben", "mike", "kia", "harry"}
don = {"mike", "kia", "sia"}

print(john, type(john))
print(jack, type(jack))

"""
S1 = john | jack  # Union
S2 = john & jack  # Intersection
S3 = john - jack  # Difference
"""

S1 = john.union(jack)         # Union
S2 = john.intersection(jack)  # Intersection
S3 = john.difference(jack)    # Difference

print(S1)
print(S2)
print(S3)

# Membership Testing
print("fionna" in john)
print("sia" not in jack)

print(don.issubset(john))
print(john.issuperset(don))

# Assignment: explore symmteric_difference on sets :)

