contacts = {
    "number": "4",
    "students": [
        {"name": "Alice", "age": 21, "email": "alica@example.com"},
        {"name": "Bob", "age": 22, "email": "bob@example.com"},
        {"name": "Charlie", "age": 23, "email": "charly@example.com"},
        {"name": "David", "age": 24, "email": "david@example.com"},
    ],
}


print("Students email list:")
for student in contacts["students"]:
    print(student["email"], "(" + student["name"] + ")")
print("Total number of students:", contacts["number"])