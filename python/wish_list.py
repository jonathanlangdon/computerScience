# determine whether you want to buy an item


def wish_list(alist, item, cost, budget):
    if item in alist and cost <= budget:
        return f"You should buy a {item}!"
    if item in alist and cost > budget:
        return f"You should save up for a {item}!"
    if item not in alist:
        return f"You probably don't want to buy a {item}."
