#Write a simple class
class dog():
    species = 'mammal'
    def __init__ (self,breed,name,spot):
        self.breed = breed
        self.name = name
        self.spot = spot
my_dog = dog(breed='lab', name='sama',spot='NO SPOTS')
print (my_dog.spot)
print (my_dog.species)