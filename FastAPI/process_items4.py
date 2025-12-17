def process_item(item: int | str):
    if isinstance(item, int):
        print("Integer: " + str(item))
    elif isinstance(item, str):
        print("String: " + item)


process_item(42)
process_item("Hello")
