def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name + ": " + str(item_price))


items_dict = {"apple": 0.99, "banana": 0.59, "cherry": 2.99}

process_items(items_dict)
