# write output file from input file


def multiply_file_by_index(output_file, input_file):
    read_file = open(input_file, "r")
    write_file = open(output_file, "w")
    lines = read_file.readlines()
    for i in range(1, len(lines) + 1):
        print(int(lines[i - 1]) * i, file=write_file)
    read_file.close()
    write_file.close()
