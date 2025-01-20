class Parrot:
     species = "bird"
     def __init__(self, name, age):
      self.name = name
      self.age = age
bew = Parrot("Bew", 10)
lue = Parrot("Lue", 15)
print("{} is {} years old".format(bew.name,bew.age))
print("and {} is {} years old.".format(lue.name,lue.age))
print("{} and {} are both {}s".format(bew.name,lue.name,bew.species))