topFive = ["Agadoo", "Mr Blobby", "Crazy Frog", "Can we Fix It", "Say Eh-Oh", "Can we Fix It"]
print(sorted(topFive))

topFive[2] = "Boom bang a bang"
topFive.insert(3, "Waterloo")
print(topFive)
song = topFive.pop(2)
print(topFive)
print(song)
