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

# model real world object example:
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}

    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")
# create instance of shopping cart called my cart.
# use add item to add an item
my_cart = ShoppingCart("Michelle")
my_cart.add_item("lemon", 2)


# == Inheritance
# one class takes on the attributes of another class (is-a relationship)
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides


# Add your Triangle class below!
class Triangle(Shape):
    # **(shape)** is the class from which the new class inherits
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3


# create new class that inherits from employee
# give class calculate_wage method that overrides employee
# return part-time employees number of hours worked multiplied by 12.00
# class Employee(object):
#     """Models real-life employees!"""
#     def __init__(self, employee_name):
#         self.employee_name = employee_name
#
#     def calculate_wage(self, hours):
#         self.hours = hours
#         return hours * 20.00


# Add your code below!
# class PartTimeEmployee(Employee):
#     def calculate_wage(self, hours):
#         print(12.00 * self.hours)

# ZAC HELP 14. THIS LOOKS LIKE A JOB FOR...
# WRONG WRONG WRONG. BUT RIGHT?
# if you need a method/attribute in the base class which was overwritten
# use super call
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00


class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        print(12.00 * self.hours)

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)


milton = PartTimeEmployee("Milton")
milton.full_time_wage(10)
print(milton.full_time_wage)

# REVIEW
print("current place")
# ZAC HELP WHAT THE HECK! *********


class Triangle(object):
    # 17
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    number_of_sides = 3

    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False


class Equilateral(Triangle):
    # 18
    angle = 60

    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle

my_triangle = Triangle(90, 30, 60)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles)

print("End of Course")
# EOC
