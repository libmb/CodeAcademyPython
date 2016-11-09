# == iteration nation

my_dict = {
    "Michelle": "Girl",
    "Zac": "Boy",
    "Rex": "dog"
}

print(my_dict.items())
# prints pairs
print(my_dict.keys())
# prints keys
print(my_dict.values())
# prints values

for key in my_dict:
    # print out key -space- value
    print(key, my_dict[key])

# == list comprehensions

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

# long example

new_list = [x for x in range(1,6)]
# creates list populated with numbers one to five
doubles = [x*2 for x in range(1,6)]
# doubles numbers
doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3 == 0]
# returns only doubled numbers that are divisible by 3

even_squares = [x**2 for x in range(1,11) if x % 2 ==0]
# use list comprehension to build list- include squares of the even numbers between 1 to 11
print(even_squares)

cubes_by_four = [x**3 for x in range(1,11) if x**3 % 4 == 0]
# create list consists of cubes of hte numbers 1-10 only if the cub is evenly divisible by four
print(cubes_by_four)

# == list slicing

l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# [start:end:stride]; start to where it ends, stride = space between
print(l[2:9:2])

my_list = list(range(1, 11))
# List of numbers 1 - 10
# Add your code below!
# print odd element start to finish
print(my_list[::2])

# examples
to_five = ['A', 'B', 'C', 'D', 'E']
print(to_five[3:])
# prints ['D', 'E']
print(to_five[:2])
# prints ['A', 'B']
print(to_five[::2])
# print ['A', 'C', 'E']


my_list = list(range(1, 11))
# Add your code below!
# create var backwards and set equal to reversed version of my list
backwards = my_list[::-1]
print(backwards)

to_one_hundred = list(range(101))
# Add your code below!
# go backwards by tens
backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)

to_21 = range(1,22)
# did not create list as example PYTHON 3 DIFF
odds = to_21[::2]
print(odds)
middle_third = to_21[7:14]
print(middle_third)

# == Lambdas

my_list = range(16)
# filter takes a function and a list and returns a new list containing all of the elements
# in the original list where the function returned true
# PYTHON THREE DIFFERENCE; LIST AND RANGE
print(list(filter(lambda x: x % 3 == 0, my_list)))

# example
def by_three(x):
    return x % 3 == 0
# same as
print(list(filter(by_three, my_list)))

languages = ["HTML", "JavaScript", "Python", "Ruby"]
# fill in filter function so that Python is the only language returned with the filter
print(list(filter(lambda x: x == "Python", languages)))

squares = [x**2 for x in range (1,11)]
# Create a list, squares, that consists of the squares of the numbers 1 to 10.
# A list comprehension could be useful here!
# Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).
print(list(filter(lambda x: x >= 30 and x <= 70, squares)))

# == Review

movies = {
	"Monty Python and the Holy Grail": "Great",
	"Monty Python's Life of Brian": "Good",
	"Monty Python's Meaning of Life": "Okay"
}
# print all items- key and value
print(movies.items())

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
# use list compre. to creat a list that consists of numbers 1-15 that is evenly divisible by 3 or 5
print(threes_and_fives)

garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
# message is backwards and we want every other letter- use slicing
message = garbled[::-2]

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
# call filter to filter out x's
message = filter(lambda x: x != "X", garbled)
print(message)

print("EOC")
# END OF COURSE


one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six  = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
print(one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve)

# print the binary version of a number:
print(bin(1))

# print int("1",2)
# print int("10",2)
# print int("111",2)
# print int("0b100",2)
# print int(bin(5),2)
# Print out the decimal equivalent of the binary 11001001.
print(int("11001001", 2))
# second optional parameter for int function
# given string with number and the base of that number, function returns the value converted to base ten

# AND (&) operator compares two numbers on a
# bit level and returns a number where the bits of that number are turned
# on if the corresponding bits of both numbers are 1
print(bin(0b110 & 0b101))

#  OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number
# are turned on if either of the corresponding bits of either number are 1
print(bin(0b1110 | 0b101))

# XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the
# bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.
print(bin(0b1110 ^ 0b101))

# NOT operator (~) just flips all of the bits in a single number.
# equivalent to adding one to the number and then making it negative.
print(~1)
print(~2)
print(~3)
print(~42)
print(~123)

# bit mask is just a variable that aids you with bitwise operations.
# A bit mask can help you turn specific bits on, turn others off, or
# just collect data from an integer about which bits are on or off.
def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    return "off"


# masks to turn a bit in a number on using |
# Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.
# Use a bitmask and the value a in order to achieve a result where the third bit from the right of a is turned on
a = 0b10111011
mask = 0b100 # bit three, not base ten 3
desired = a | mask
print(bin(desired))


# XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the
# number one will return a result where that bit is flipped.
# Use a bitmask and the value a in order to achieve a result where all of the bits in a are flipped.
a = 0b11101110 # 8 bit variable
mask = 0b11111111 # mask same length in which all bits are turned on
desired = a ^ mask
print(bin(desired))


#  you can also use the left shift (<<) and right shift (>>) operators to slide masks into place
# Define a function called flip_bit that takes the inputs (number, n).Flip the nth bit (with the ones bit
# being the first bit) and store it in result. Return the result of calling bin(result).
def flip_bit(number,n):
    mask = 0b1 << (n - 1)
    result = number ^ mask
    return bin(result)


print("EOC")
# === END OF COURSE
