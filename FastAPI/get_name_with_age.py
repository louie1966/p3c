def get_name_with_age(name: str, age: int):
    name_with_age = name.title() + " is " + str(age) + " years old."
    return name_with_age


print(get_name_with_age("john", 30))
print(get_name_with_age("jane", 25))
