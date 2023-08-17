# take a list of tuples and return a tuple of lists using a for loop


def sort_artists(alist):
    artists = []
    revenues = []
    for artist, revenue in alist:
        artists.append(artist)
        revenues.append(revenue)
    artists.sort()
    revenues.sort(reverse=True)
    return (artists, revenues)
