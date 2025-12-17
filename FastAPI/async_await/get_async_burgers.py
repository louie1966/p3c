import asyncio

async def get_burgers(number: int):
    # Do some asynchronous stuff to create the burgers
    burgers = number * ["🍔"]
    return burgers

async def main():
    print(await get_burgers(3))  # Example usage in an async context

asyncio.run(main())

