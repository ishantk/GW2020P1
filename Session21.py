"""

    Multi Threading in Python

    In our Programs, their are code snippet which may take longer time than usual
    Hence, execution of the program is halted for a time duration
    and if that time duration is nearly 3 to 5 seconds, user experiences is degraded

    OS will give a message: Would You like to wait or Kill the App ?

    Hence, we need to think of long running operation

"""

import requests
import threading    # built in module from python

"""
class FetchHealthNews:

    def fetch(self):
        print("Fetch News Started")
        url = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=31c21508fad64116acd229c10ac11e84"
        response = requests.get(url)
        print(response.text)
        print("Fetch News Finished")
"""

#Inheritance: FetchHelthNews is now the Child of Thread
class FetchHealthNews(threading.Thread):

    # Overriding the Function from the Parent class
    # For a Child Thread, we must write long running operations in run function
    def run(self):
        print("Fetch News Started")
        url = "http://newsapi.org/v2/top-headlines?country=in&category=health&apiKey=31c21508fad64116acd229c10ac11e84"
        response = requests.get(url)
        print(response.text)
        print("Fetch News Finished")


# whatever we write in main is executed in a sequence
def main():
    print("App Started")

    fRef = FetchHealthNews()
    # fRef.fetch()                # This may become a long running operation due to Internet Connectivity

    fRef.start()                  # This shall execute run function internally and will make it execute parallel to the main

    # Doing Some Operation
    for i in range(1, 11):
        print("i is:", i)

    print("App Finished")


if __name__ == '__main__':
    main()


# Asynchronous Programming: i.e. main and FetchNews Operations is running together
#                                majorly we say FetchNews Operation is in the background and main is in the foreground