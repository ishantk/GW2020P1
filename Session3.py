# Single Value Container
instagram_id = "auribises"
print("instagram_id is:", instagram_id)
print("instagram_id hashcode is:", id(instagram_id))

anyName = "auribises"
print("anyName is:", instagram_id)
print("anyName hashcode is:", id(instagram_id))

# instagram_id and anyName are Reference Variables
# They hold the hashcode fof the Data :)

# Multi Value Container
# Tuple:      0         1         2        3      4
followers = "john", "jennie", "fionna", "dave", "kia"
print("Followers Are:", followers)
print("Followers hashCode is:", id(followers))

print(followers[0], id(followers[0]))

# Change the id of a follower
# followers[0] = "john.watson" # Error

# Kia would like to unfollow
# del followers[4] # Error

# Tuple as a Multi Value Container is IMMUTABLE
# Once it is created it gets fixed and we cannot change it
# i.e. add, update and delete operations wont work

