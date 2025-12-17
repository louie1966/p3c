def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Who are you?")


say_hi("Alice")
say_hi()
