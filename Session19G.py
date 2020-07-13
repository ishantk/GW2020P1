import requests
import json

url = "https://api.covid19india.org/data.json"

response = requests.get(url)

# convert JSON Data into Python Dictionary
covid_data = json.loads(response.text)

print(covid_data["statewise"])

covid_cases_india = []

for i in range(0, len(covid_data["statewise"])):
    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print(covid_data["statewise"][i]["state"])
    print(covid_data["statewise"][i]["active"])
    print(covid_data["statewise"][i]["confirmed"])
    print(covid_data["statewise"][i]["deaths"])

    covid_cases_india.append(
        {
            "state": covid_data["statewise"][i]["state"],
            "active": covid_data["statewise"][i]["active"],
            "confirmed": covid_data["statewise"][i]["confirmed"],
            "deaths": covid_data["statewise"][i]["deaths"],
        }
    )

    print("~~~~~~~~~~~~~~~~~~~~~~~~")
    print()

# Implement Search Sort and Filter After this program where we are fetching Real Time Results
# Explore https://developers.zomato.com/ for JSON Parsing :)

print(covid_cases_india)
print(len(covid_cases_india))