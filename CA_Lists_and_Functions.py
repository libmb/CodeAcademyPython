# List accessing; write code to print second element:
n = [1, 3, 5]
print(n[1])

# list element modification; multiply second element of n by 5; overwrite second element with that result

n[1] = n[1] * 5
print(n)

# append to list; add 4 to list n:

n.append(4)
print(n)

# removing elements from list
# n.pop(index) | removes index, returns index
# n.remove(item) | removes specific item if found
# del(n[index]) | removes index, does not return

del(n[0])
print(n)

# changing the functionality of a function; change the function so the argument is multiplied by 3 and returned

number = 5


def my_function(x):
    #here I changed + to *
    return x * 3

print(my_function(number))

# more than one argument; define function with 2 parameters:

m = 15
n = 13


def addd_function(x,y):
    return x + y
print(addd_function(m, n))

# strings in functions; write function that takes string as argument and returns argument concatenated with the word 'world'

n = "Hello"


def string_function(s):
    return s+'world'
print(string_function(n))

#you pass a list to a function the same way you pass an argument to a function:


def list_function(x):
    return x

n = [3, 5, 7]
print(list_function(n))

# passing a list to a function stores it in the argument just like a string or number:


def list_function2(x):
    return x[1]

print(list_function2(n))

# modifying an element of a list in a function; add 3 to index one and return new list:


def list_function3(x):
    x[1] = x[1]+3
    return x

print(list_function3(n))

# list manipulation in fuctions; append number 9 to list:


def list_extender(lst):
    lst.append(9)
    return lst

print(list_extender(n))

# printing out a list item by item in a function:


def print_list(x):
    for i in range(0, len(x)):
        print(x[i])

print(print_list(n))

# modifying each element in a list in a function; multiply by 2 and return list:

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print(double_list(n))

# passing a range into a function: start up to but NOT including the stop- each item increases by STEP*
# range(stop)
# range(start, stop)
# range( start, stop, step*)


def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
# new for python 3; range must be list
print(my_function(list(range(0,3))))

# iterating over a list in a function

n = [3, 5, 7]


def totalx(numbers):
    result = 0
    for num in numbers:
        result = result + num
    return result

print(totalx(n))

# using strings in lists in functions


n=["Michael", "Lieberman"]


def join_strings(words):
    result = ""
    for name in words:
        result = result+name
    return result
print(join_strings(n))

# Using two lists as two arguments in a function:

m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y):
    return x + y

print(join_lists(m,n))

# using a list of lists in a function

n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]


def flatten(lists):
    results = []
    for numbers in lists:
        for num in numbers:
            results.append(num)
    return results

print(flatten(n))

# end of lesson