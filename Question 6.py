#Something that is mutable
camping_stuff = ["tent", "sleeping bag", "water", "knife", "coffee", "flash drive", "stove", "oil", "food","Ball"]

me = camping_stuff[3] + " and " + camping_stuff[5]
print(me)

you = camping_stuff[-4]
print(you)

camping_stuff.append("Toilet Paper")
camping_stuff.append("Bidet")

camping_stuff.extend(["Toilet Paper", "Bidet"])
print(camping_stuff)

#Something that is Immutable
print("Hello there my friend what is your name?")
