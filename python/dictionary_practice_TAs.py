# create a dictionary from a list and access the dictionary


ta_info = [("Joshua", "Georgia"), ("Jackie", "Vermont"), ("Marguerite", "Tennessee")]

ta_dict = {}
for tuple in ta_info:
    (name, state) = tuple
    ta_dict[name] = state

josh_val = ta_dict["Joshua"]
jack_val = ta_dict["Jackie"]
marg_val = ta_dict["Marguerite"]
