class Car:
    def __init__(self, make="Ford", model="Fiesta", colour="Silver"):
       self.make = make
       self.model = model
       self.colour = colour
       self.speed = 0

    def accelerate(self, increment):
        self.speed += increment

    def brake(self, increment):
        self.speed -= increment

    def __str__(self):
        return f"I am a {self.colour} {self.make} {self.model} travelling at {self.speed}mph."