# functions

def requirements(height, age):
    return height * age
    

print(requirements(11, 3))

# if-else
classes = ["alpha", "beta", "ceta"]

if classes[1] == "alpha":
    print("good guess")

elif classes[1] == "beta":
    print("Right")
else:
    print("youre wrong")

classes.append("school")
print(classes)

classes.insert(1, "mama")
print(classes)



#classes
class vehicle:
    def __init__(self, name, brand):
        self.name = name
        self.brand = brand

    def showcase(self, target):
        print(f"{self.brand} is currently in {target}'s shop")

doggy = vehicle("mercedes", "AMG") # create an object
doggy.showcase("john") # call method on object

class bike(vehicle):
    def __init__(self, name, brand, type, material):
        super().__init__(name, brand)
        #making the type attribute protected by adding _ before it. 
        self._type = type
        #making material a private attribute by adding __ before it.
        self.__material = material
    
    #making the details method protected by adding _ before it.
    def _details(self, target):
        print(f"{self.name} is a {self._type} bike mode for {self.__material} in {target}'s collection")
my_bikey = bike("speedster", "yamaha", "mountain", "carbon fiber")
my_bikey._details("john")
# how to change values in a class
my_bikey.__material = "aluminum"
my_bikey._details("john")
#accessing protected attribute
print(my_bikey._type)

# data hiding. hiding attributes. keeping unintended modifications away
# attributes with single underscore _ are protected attributes, signaling that they should not be accessed directly outside the class or its subclasses.
# attributes with double underscore __ are private attributes, making them inaccessible from outside the class.
# calling private attribute outside the class will raise an AttributeError
print(my_bikey.__material)  # This will raise an AttributeError
# to access private attribute, we can use name mangling
print(my_bikey._bike__material)  # Accessing private attribute using name mangling.
# however, it is not recommended to access private attributes this way as it breaks encapsulation principles.
# methods can also be made private by using double underscores before their names, and protected methods can be made using a single underscore before their names.