# sort 2 dictionaries and combine into one dictionary


def stars(movies, tvshows):
    actor_dict = {}
    for movie, actors in movies.items():
        for actor in actors:
            if actor not in actor_dict:
                actor_dict[actor] = []
            actor_dict[actor].append(movie)
    for show, actors in tvshows.items():
        for actor in actors:
            if actor not in actor_dict:
                actor_dict[actor] = []
            actor_dict[actor].append(show)
    for actor, appearances in actor_dict.items():
        actor_dict[actor] = sorted(appearances)
    return actor_dict
