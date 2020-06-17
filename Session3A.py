# MVC with () or no bracket is TUPLE
# followers = ("john", "jennie", "fionna", "dave", "kia")
# print(followers, type(followers), len(followers))

# MVC with [] is List
followers = ["john", "jennie", "fionna", "dave", "kia"]
print(followers, type(followers), len(followers))

# List is MUTABLE
# We can add update and delete i.e. changes are supported
# The way you add data it gets stored in indexing

# Update id of a follower
followers[0] = "john.watson"
print(followers, type(followers), len(followers))

# Delete a Follower from the List
del followers[3]
print(followers, type(followers), len(followers))

# Add New Followers
followers.append("harry")
followers.append("george")
followers.append("Kim")

print(followers, type(followers), len(followers))

# In Computer Science Terms : Tuple and List are Data Structures

# Challenge with the List
# List Supports Duplicates

followers.append("fionna")
followers.append("john.watson")

print(followers, type(followers), len(followers))


