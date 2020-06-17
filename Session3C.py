johnsFollowers = {"kia", "sim", "leo", "mike", "dave"}
fionnasFollowers = {"john", "kia", "lee", "Ana", "mike", "dave"}

# Mutual Friends/Followers
mutualFollowers = johnsFollowers.intersection(fionnasFollowers)

print("JOHN")
print(johnsFollowers, len(johnsFollowers))

print("FIONNA")
print(fionnasFollowers, len(fionnasFollowers))

print("MUTUAL")
print(mutualFollowers, len(mutualFollowers))