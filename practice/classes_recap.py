# create a class called "Animal" that has the following attributes:
# - name
# - age
# - species
# - color
# inside the class, create the following methods:
# - __init__ (initialize the attributes)
# - get_name (returns the name of the animal)
# - get_age (returns the age of the animal)
# - get_species (returns the species of the animal)

class Animal:
    def __init__(self, name, age, species, color):
        self.name = name
        self.age = age
        self.species = species
        self.color = color

    def get_name(self):
        return self.name

    def get_age_and_name(self):
        # return the name of the animal and the age
        return f"{self.name} is {self.age} years old"

    def get_species(self):
        return self.species

    def get_color(self):
        return self.color


# instantiate an object of the Animal class
# assign it to a variable called "animal"
# pass the following arguments to the __init__ method:
# - name: "Lion"
# - age: 5
# - species: "Mammal"
# - color: "Brown"
animal = Animal("Lion", 5, "Mammal", "Brown")
