# practice creating instances of classes that are nested


class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label


class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist


taylor_swift = Artist("Taylor Swift", "Big Machine Records, LLC")

song_1 = Song("You Belong With Me", "Fearless", 2008, taylor_swift)

song_2 = Song("All Too Well", "Red", 2012, taylor_swift)

song_3 = Song(
    "Up We Go", "Midnight Machines", 2016, Artist("LiGHTS", "Warner Bros. Records Inc.")
)
