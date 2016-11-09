# intro:
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))

    def is_edible(self):
        if not self.poisonous:
            print("Yep! I'm edible.")
        else:
            print("Don't eat me! I am super poisonous.")

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()

# outside of the class; create a variable named zebra and set it equal to Animal("Jeffrey")
# print out zebra's name
class Animal(object):
    def __init__(self, name):
        self.name = name

zebra = Animal("Jeffrey")
print(zebra.name)

# add third attribute, is_hungry
# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, hungry):
        self.name = name
        self.age = age
        self.is_hungry = hungry

# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)


# each individual animal gets its own name and age
# but all have access to variable is_alive
# some functions are availabel everywhere, some to members
# of certain class, and others in particular instances:
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print(zebra.name, zebra.age, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_alive)
print(panda.name, panda.age, panda.is_alive)

# add method description that uses 2 print statements to print attributes
# create instance of anmial and call its description
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(self):
        print(self.name)
        print(self.age)

hippo = Animal("Hally", "3")
hippo.description()
# add two animals
# print health of three animals
sloth = Animal("Sally", "5")
ocelot = Animal("Lotty", "2")
print(hippo.health)
print(sloth.health)
print(ocelot.health)



