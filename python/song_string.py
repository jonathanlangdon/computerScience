# create a function that returns properties of an instance of a class


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


def get_song_string(song):
    return f'"{song.name}" - {song.artist.name} ({song.year})'
