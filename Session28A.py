import requests
from bs4 import BeautifulSoup


class Team:

    def __init__(self, year, team_name, matches, won, lost, tied, anandoned, points, net_run_rate):
        self.year = year
        self.team_name = team_name
        self.matches = matches
        self.won = won
        self.lost = lost
        self.tied = tied
        self.anandoned = anandoned
        self.points = points
        self.net_run_rate = net_run_rate

    def __str__(self):
        return "{},{},{},{},{},{},{},{},{}\n".format(
            self.year, self.team_name, self.matches, self.won, self.lost, self.tied, self.anandoned, self.points, self.net_run_rate)


class FetchTeamsData:

    def fetchData(self, year, save_data):

        url = "https://www.espncricinfo.com/table/series/8048/season/{}/ipl".format(year)

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

        # represents list index in the list
        i = 0
        j = 0

        for tag in team_data_tags:
            team_data[i].append(float(tag.text.strip()))

            j += 1

            if j % 6 == 0:
                i += 1

        for tag in team_points_tags:
            team_points.append(float(tag.text.strip()))

        # print(len(team_names))
        # print(len(team_data))
        # print(len(team_points))

        teams = []

        for i in range(len(team_names)):

            team = Team(year, team_names[i], team_data[i][0], team_data[i][1],
                        team_data[i][2], team_data[i][3], team_data[i][4], team_points[i], team_data[i][5])

            teams.append(team)



        if save_data:
            file = open("IPL-TEAMS-DATA-{}.csv".format(year), 'a')

            for team in teams:
                print(team)
                file.write(str(team))

            print("DATA-SAVED-IN-FILE")

        else:
            for team in teams:
                print(team)


def main():

    data = FetchTeamsData()
    data.fetchData(2019, True)


if __name__ == '__main__':
    main()

# Assignment: Plotting the data on Graphs using matplotlib