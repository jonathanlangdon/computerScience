# add error handling to indexing code

a_list = [1, 2, 3, 4, 5]
list_index = "d"


print("Accessing index...")
try:
    result = a_list[list_index]
    print("Value at index:", result)
except IndexError:
    print("Invalid index!!")
except:
    print("Unknown error!")
print("Done!")
