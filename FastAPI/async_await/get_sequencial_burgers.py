# This is not asynchronous
def get_sequential_burgers(number: int):
    # Do some sequential stuff to create the burgers
    burgers = number * ["🍔"]
    return burgers


print(get_sequential_burgers(3))
