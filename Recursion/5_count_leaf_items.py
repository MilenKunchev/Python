ll = ["Adam", ["Bob", ["Tom", "Peter"], "Peter"], "Mike"]


def count_leaf_items(ll):
    """
    Recursively count and return the
    number of leaf items in a nested list
    """
    count = 0
    for item in ll:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            count += 1
    return count


print(len(ll))
print(count_leaf_items(ll))
