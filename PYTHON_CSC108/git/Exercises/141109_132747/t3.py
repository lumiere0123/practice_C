#Define a class Pet that contains three object (instance) variables: name, species, and age. 
#The constructor for Pet should take arguments (in the listed order) that initialize these variables.

class Pet(object):
    
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age
    

