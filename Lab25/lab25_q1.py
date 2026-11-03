class Car:
    def __init__(self,make,model,year,color,started=False,speed=0,max_speed=200):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.started=started
        self.speed=speed
        self.max_speed=max_speed

    showroom = "NewAge"
    @classmethod
    def change_showroom(cls, name):
        cls.showroom = name

    def __str__(self):
        return f"{self.make} {self.model} {self.color} ({self.year})"

    @staticmethod
    def show_intro_message():
        print("This class represents a car")

#a
toyota_camry=Car("Toyota","Camry",2022,"Black")
print(toyota_camry.make)
print(toyota_camry.model)
print(toyota_camry.year)
print(toyota_camry.color)
print(toyota_camry.started)
print(toyota_camry.speed)
print(toyota_camry.max_speed)

#b
ford_mustang=Car("Ford","Mustang",2022,"Black")
print(ford_mustang.make)
print(ford_mustang.model)
print(ford_mustang.year)
print(ford_mustang.color)
print(ford_mustang.started)
print(ford_mustang.speed)
print(ford_mustang.max_speed)

#c
#print(Car.make)
#Attribute Error because make is an instance attribute. It is created using self.make when an object is initialized, not directly inside the class namespace.
print("make" in toyota_camry.__dict__)
print("make" in ford_mustang.__dict__)

#d
print(Car.__dict__)
#Car.__dict__ displays the namespace of the Car class. It contains special attributes such as __module__, __init__, and __doc__. The __static_attributes__ tuple lists attribute names accessed through self in the class's methods. Instance attributes such as color, make, and speed are stored in the instance's __dict__, not directly in the class's dictionary.

#e
print(Car.showroom)
Car.change_showroom("Premium equipments")
print(Car.showroom)
print(Car.__dict__)
#Output is NewAge and then Premium equipments
#.__dict__ statement now prints the class dictionary, including showroom with its updated value and the change_showroom method.

#f
print(toyota_camry.__dict__)
#toyota_camry.__dict__ contains the instance's attribute whereas Car.__dict__ contains the class level members including methods and class attributes.

#g
print(str(toyota_camry))
print(str(ford_mustang))

#h
Car.show_intro_message()