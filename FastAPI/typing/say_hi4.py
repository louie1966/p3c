def say_hi(name: str | None):
    print(f"Hey {name}!")


say_hi("Alice")
say_hi(None)
say_hi("Bob")
say_hi("")  # Testing with an empty string
