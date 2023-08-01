# sort a file with list of movies by revenue


def sort_films(source_file, dest_file):
    open_file_r = open(source_file, "r")
    open_file_w = open(dest_file, "w")
    movie_list = []
    for line in open_file_r:
        (movie, revenue) = line.split("\t")
        movie_list.append((movie, int(revenue)))
    open_file_r.close()
    movie_list.sort(key=lambda x: x[1], reverse=True)
    for item in movie_list:
        (movie, revenue) = item
        print(movie + "\t" + str(revenue), file=open_file_w)
    open_file_w.close()
