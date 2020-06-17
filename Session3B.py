# {} -> Braces
followers = {"john", "jennie", "fionna", "dave", "kia"}
print(followers, type(followers), len(followers))

# Set wont support duplicates
# Set add the data with hashing and hence we cannot see the output the way we added
# It shall come as per the buckets

# Add Data
followers.add("fionna")
followers.add("george")
followers.add("harry")
followers.add("kia")
followers.add("john")

print(followers, type(followers), len(followers))

# Remove Data
followers.remove("kia")
print(followers, type(followers), len(followers))

# Assignment -> How will you update the john to john.watson in the Set ?

