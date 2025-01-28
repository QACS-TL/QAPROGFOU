class Animal:
    animal_type = "mammal"
    animal_colour = "grey"
    def eat(self, food):
        print(f"I'm an {self.animal_type} eating {food}")


ani1 = Animal()
ani1.animal_type = "Elephant"
ani1.animal_colour = "Grey"

ani2 = Animal()
ani2.animal_type = "Whale"
ani2.animal_colour = "Blue"

print(ani1.animal_type, ani1.animal_colour)
print(ani2.animal_type, ani2.animal_colour)
ani1.eat("buns")
ani2.eat("fish")

animals = {"elephant":"large, grey animal with a long nose"
    , "frog":"small(ish) animal with flippers, jumps a lot"
    , "anteater":{"defn":"middlish sized animal with long snout to hoover up ants", "food":"ants", "health":"67"}}

print(animals["frog"])

animals["aardvark"] = "Cute, when small, with scales on its back"

animals["frog"] = "Green and slippery"

print(animals)

my_animal_set = {"cat", "dog", "mouse", "cat"}
my_pets_set = {"cat", "dog", "hamster"}
print(my_animal_set.intersection(my_pets_set))

topFive = ["Agadoo", "Mr Blobby", "Crazy Frog", "Can we Fix It", "Say Eh-Oh", "Can we Fix It"]

top_five_no_duplicates = list(set(topFive))
print(top_five_no_duplicates)