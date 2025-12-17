def get_full_name(first_name: str, last_name: str):
    full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


print(get_full_name("john", "doe"))
print(get_full_name("jane", "smith"))
