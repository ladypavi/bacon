name = "Pavi"
print("hello world")
print("hello Pavi")
#print("hello " + name)
print("hello %s" % name)

if name == "Pavi":
    print("Yay!")
else:
    print("Boo!")

groceries = ["Lettuce", "Tomato", "Bacon"]
print(groceries)

for i in groceries:
    print(i)
    if i == "Bacon":
        print("Yummy yummy in my tummy!")

groceries.append("Mayo")

for i in groceries:
    print(i)
    if i == "Mayo":
        print("Blech!")

bad_mayo = groceries.index("Mayo")

groceries[bad_mayo] = "Mustard"

print(groceries)

print(":'(")