"""
    Webscrapping ESPN CricInfo IPL Data
    Creating DataSet for Cricket

"""

import requests
from bs4 import BeautifulSoup

url = "https://www.espncricinfo.com/table/series/8048/season/2019/ipl"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

team_name_tags = soup.find_all("h5", class_="header-title label")
team_data_tags = soup.find_all("td", class_="")
team_points_tags = soup.find_all("td", class_="border-right label")


team_names = []
team_data = []
team_points = []

for tag in team_name_tags:
    team_names.append(tag.text.strip())
    team_data.append([])

# some Heading for IPL and not the tean
del team_names[0]
del team_data[0]



print("*******************")

# represents list index in the list
i = 0
j = 0

for tag in team_data_tags:
    print(tag.text)
    team_data[i].append(float(tag.text.strip()))

    j += 1

    if j % 6 == 0:
        i += 1
        print("--------")



print("*******************")

for tag in team_points_tags:
    team_points.append(float(tag.text.strip()))


print(team_names)
print(team_data)
print(team_points)


