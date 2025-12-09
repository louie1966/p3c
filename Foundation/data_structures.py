print("**** Lists ****\n")

l = ["first", "second"]

print(type(l))

print(l[0])

l.append("fourth")
l.insert(2, "third")
l.remove("first")

print(l)

print("\n**** Tuples ****\n")
t = ([1, 2, 3], "second", 3.0)
t[0].append(4)

print(type(t))
print(t[1])
print(t)


print("\n**** Sets ****\n")
s = {1, 2, 3}
s.add(4)
s.add(5)
s.add(2)  # Duplicate, will have no effect
s.remove(1)

print(type(s))
print(5 in s)
print(s)

print("\n**** Dictionaries ****\n")
d = {"item": "laptop", "quantity": 10, "price": 400.00}
print(d)
print(d.keys())
print(d.values())
print(d.pop("price"))
d["quantity"] = 15
d["discount"] = 0.1
d["price"] = 350.00
print(d["item"])
print(d)
