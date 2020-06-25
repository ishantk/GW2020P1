S1 = {10, 20, 30, 40, 50}
S1.add(90)
print(S1)

S1.remove(20)
print(S1)

S1.pop()
print(S1)

# S1.clear() # Remove All

# Convert Set into the List
L1 = list(S1)
print(L1, type(L1))

S2 = str(S1)
print(S2, type(S2))