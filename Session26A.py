import requests
import json
import matplotlib.pyplot as plt

url = "https://api.covid19india.org/data.json"
response = requests.get(url)
# print(response.text)

# loads takes json and gives back python dictionary
covid_cases = json.loads(response.text)
# print(covid_cases)

covid_cases_time_series = covid_cases['cases_time_series']
# print(covid_cases_time_series)

total_confirmed = []
for case in covid_cases_time_series:
    # data = int(case['totalconfirmed'])
    # print(data)
    total_confirmed.append(int(case['totalconfirmed']))

print(len(total_confirmed))
print(total_confirmed[172])

plt.plot(total_confirmed)
plt.show()

# matplotlib assignment: draw graphs for all the states