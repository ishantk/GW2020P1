"""
    Circular Doubly Linked List
        Has-A Relationship
        Gaana App Play List Use Case

    Inheritance in OOPS
        What is Inheritance
        Why we Need it
"""

# attributes: title, artists, duration, next_song, previous_song
class Song:

    def __init__(self, title, artists, duration):
        self.title = title
        self.artists = artists
        self.duration = duration

    def show(self):
        print("----------------------------------------------")
        print("{}\t\t{}\t\t{}".format(self.title, self.artists, self.duration))
        print("----------------------------------------------")


def main():

    song1 = Song("1. Meri Ashiqui", "Rubin, Jubin", 4.55)
    song2 = Song("2. Yalgar", "Aroob, Jubin", 5.55)
    song3 = Song("3. Genda Phool", "Rubin, Zara", 4.33)
    song4 = Song("4. Cute Song", "Tony, Mohit", 2.6)
    song5 = Song("5. Goa Beach", "Rubin, Mohit", 3.44)

    song1.next_song = song2
    song2.next_song = song3
    song3.next_song = song4
    song4.next_song = song5
    song5.next_song = song1

    song1.previous_song = song5
    song2.previous_song = song1
    song3.previous_song = song2
    song4.previous_song = song3
    song5.previous_song = song4


    current_song = song1

    while current_song != song5:
        current_song.show()
        current_song = current_song.next_song


    print()

    current_song = song5
    while current_song != song1:
        current_song.show()
        current_song = current_song.previous_song


    # Assignment: Cant see 1 song in both logics. Please fix it :)

if __name__ == '__main__':
    main()