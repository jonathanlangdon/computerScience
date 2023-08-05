# sort a dictionary by its values and return top result


def most_oscars(nominations):
    sorted_actors = sorted(nominations.items(), key=lambda item: item[1], reverse=True)
    return sorted_actors[0]
