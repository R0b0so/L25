class Dog:
     species = "dog"
     def __init__(self, name, age, color):
      self.name = name
      self.age = age
      self.color = color
German_Shepard = Dog("ruff", 6, "gray")
Golden_Retriver = Dog("rocky", 10, "yellow")
print("{} is {} years old".format(German_Shepard.name,German_Shepard.age))
print("and {} is {} years old.".format(Golden_Retriver.name,Golden_Retriver.age))
print("{} and {} are both {}s".format(German_Shepard.name,Golden_Retriver.name,Golden_Retriver.species))
print("{} is {} and {} is {}".format(German_Shepard.name,German_Shepard.color,Golden_Retriver.name,Golden_Retriver.color))
