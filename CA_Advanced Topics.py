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

