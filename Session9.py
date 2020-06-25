"""
    String
    Set
    Dictionary
"""

# restaurant_name = 'Johns Coffee Shop'
# restaurant_name = 'John's Coffee Shop' # error
# restaurant_name = 'John\'s Coffee Shop' # escaping ' character
# restaurant_name = "John's Coffee Shop"

# RAW STRING: No Escape Characters will be treated as logic, they will be part of String data
# Whenever we wish to search something in the String
restaurant_name = r'John\'s Coffee Shop'
print(restaurant_name, type(restaurant_name))

# quote = "Work Hard, Get Luckier\nBe Exceptional"
quote = R"Work Hard, Get Luckier\nBe Exceptional" # Raw String
print(quote)

# \ breaking of string into multiple lines of code, not as in the String
message = "We are learning Python" \
          "This is an Awesome Day" \
          "Lets Code"

print(message)

# To Create a Multi Line String
my_message = """Keep Learning
Work Hard
Code Well
Be Successful
"""

print(my_message)