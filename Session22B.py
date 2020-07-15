# Regular Expressions
import re

chat_text_message = "Hello, This is John. I hope You are having a good time"

# Match Matches from the beginning
# result1 = re.match("Hello", chat_text_message)
# result2 = re.match("John", chat_text_message)

result1 = re.search("Hello", chat_text_message)
result2 = re.search("John", chat_text_message)

print(result1)
print(result2)

if result1 is not None:
    print("Hello Searched in the text message")

if result2 is not None:
    print("John Searched in the text message")


quote = "Search the candle rather than cursing the darkness"
print(quote)

# result3 = re.findall("the", quote)
result3 = re.findall(r"the", quote) # if we have any special characted -> it becomes part of data
print(result3) # list -> 3 the

# substitute is to replace
result4 = re.sub("the", "a", quote)
print(result4)

data = re.search("\w", quote)
print(data)


# Reference Study:
# https://www.regexpal.com/
# https://www.vogella.com/tutorials/JavaRegularExpressions/article.html


# Use Regular Expressions to solve the below problem statements
# 1. Extract all the words from a String
# 2. Check how many numbers are their in the String
# 3. Check if a phone number entered by user is correct
# 4. Check if email entered by user us correct
# 5. Check if date of birth is in the format dd/mm/yyyy
# 6. Check if vehicle number is in the format of PB10BD1123 -> 2chars2nums2chars4nums | 10 in length




