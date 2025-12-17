def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


items_tuple = (1, 2, "item")
items_set = {b"item1", b"item2"}
result = process_items(items_tuple, items_set)

print(result)
