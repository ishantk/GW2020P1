# Web Scrapping
import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt

url = "https://www.imdb.com/india/top-rated-indian-movies/"
# url = "https://www.espncricinfo.com/table/series/8048/season/2019/ipl" | Please Explore
response = requests.get(url)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

movieNameTags = soup.find_all("td", class_="titleColumn")
movieRatingTags = soup.find_all("td", class_="ratingColumn imdbRating")

movieTitles = []
movieYears = []
movieRatings = []

for tag in movieNameTags:
    # print(tag)
    # print(tag.text)
    # print(tag.text.strip())

    title = tag.text.strip()
    year = int(title[-5:-1])

    movieTitles.append(title)
    movieYears.append(year)


print()

for tag in movieRatingTags:
    # print(tag)
    # print(tag.text)
    # print(tag.text.strip())
    rating = float(tag.text.strip())
    movieRatings.append(rating)

print()

print(len(movieNameTags), len(movieRatingTags))


# plt.barh(movieYears, movieRatings)
# plt.plot(movieYears, movieRatings)
plt.scatter(movieYears, movieRatings)
plt.show()

# Assignment : Compare movies of India with 2 more countries
#              Try comparing them with a line graph
