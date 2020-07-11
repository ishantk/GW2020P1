# to send http network request and get the data back
import requests
import json

api_key = "Your_Api_Key"
url = "http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={}".format(api_key)
response = requests.get(url)
print(response.text)
print(type(response.text)) # string format and is a dictionary -> JSON

# convert JSON Data into Python Dictionary
news_data = json.loads(response.text)

# JSON Parsing: Extracting meaningful data from JSON
"""
print(news_data["status"])
print(news_data["totalResults"])

print(news_data["articles"][0])
print(news_data["articles"][0]["title"])
print(news_data["articles"][0]["author"])
"""

for i in range(0, len(news_data["articles"])):
    print(news_data["articles"][i]["title"])
    print(news_data["articles"][i]["author"])
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print()
