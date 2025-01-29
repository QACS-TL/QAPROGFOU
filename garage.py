from car import Car

c1 = Car("Vauxhall", "Corsa", "Blue")
c1.colour = "Purple"

c2 = Car()

c3 = Car(model="Beetle")
#c3.make = "Volkswagon"
#c3.colour = "Orange"

print(c1.colour)
print(c2.colour)
print(c3.colour)

c1.accelerate(10)
c2.accelerate(30)
c3.accelerate(70)

print(f"c1: {c1.speed}")
print(f"c2: {c2.speed}")
print(f"c3: {c3.speed}")

#garage = [c1, c2, c3]
garage = []
garage.append(c1)
garage.append(c2)
garage.append(c3)

for c in garage:
    c.accelerate(20)

for c in garage:
    print(c.speed)

for c in garage:
    print(c)

