zoo = ("wolf", "fox")
print(zoo.index("fox"))
print(zoo)
if "wolf" in zoo:
	print("wolves are one of my favorite animals")
(wolf, fox) = zoo
print(wolf)
zoo_list = list(zoo)
zoo_list.extend(["sloth", "dog", "beaver"])
zoo = tuple(zoo_list)
print(zoo)