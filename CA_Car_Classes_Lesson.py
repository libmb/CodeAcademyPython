class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"

###

my_car = Car("DeLorean", "silver", 88)
print(my_car.display_car())
print(my_car.condition)
my_car.drive_car()
print(my_car.condition)

# inheritance; add class for electric car.
# override method...


class Car(object):
    condition = "new"

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        super(ElectricCar, self).__init__(model, color, mpg)
        self.battery_type = battery_type

    def drive_car(self):
        # override method
        self.condition = "like new"


my_car = ElectricCar("Explorer", "Black", 88, "molten salt")
print(my_car.display_car())
print(my_car.condition)
my_car.drive_car()
#overrode method
print(my_car.condition)

# Representation --- ASK ZAC

class Point3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "(%d, %d, %d)" % (self.x, self.y, self.z)


my_point = Point3D(1, 2, 3)
print(my_point)

print("End of Course")
# EOC
