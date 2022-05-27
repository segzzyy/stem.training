#OOP
#Defining a class and its attributes.
#creating instances (objects) of a class.
#class methods(functions belonging to a class).
#inheritance and polymorphism.
#method overriding.

from turtle import color


class Dog :
        def __init__(self,no_of_eyes,color):
         self.no_of_eyes=no_of_eyes
         self.color=color
german_shepherd=Dog(no_of_eyes=2,color='grey')
dodger=Dog(color='whte',no_of_eyes=1)
dobberman=Dog(2,'brown')

print(german_shepherd.color)
print(dobberman.no_of_eyes)
print(dodger.no_of_eyes,dodger.color)

dobberman.color ='dark-brown'

print(dobberman.color)
class Dog :
    def bark(self):
      print("Woof woof!")
    def __init__(self,gender,bark):
     self.gender=gender
     self.bark=bark 
german_shepherd=Dog(gender='female',bark="woof woof!")
dobberman=Dog(gender='male',bark="hooo hooo")
print(german_shepherd.gender)
print(german_shepherd.bark)
print(dobberman.bark)

