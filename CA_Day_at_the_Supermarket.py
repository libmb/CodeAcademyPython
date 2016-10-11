# for loop refresh; print all elements in list names:
names = ["Adam", "Alex", "Mariah", "Martine", "Columbus"]
for x in names:
    print(x)

# for loop with keys; print all definitions of dictionary:
webster = {
    "Aardvark": "A star of a popular children's cartoon show.", "Baa": "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}
for key in webster:
    print(webster[key])

# control flow and looping;loop through items and print if number is even:
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 == 0:
        print(number)

# lists and functions; write a function that counds how many times the string "fizz" appears in a list:


def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count

print (fizz_count(["fizz", "cat", "fizz", "bear"]))

# string looping; example of looping through string:
for letter in "Codecademy":
    print(letter)

print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print(letter)

# Your own store;
# create dictionary called prices using {} format:
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
# create dictionary called stock:
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
# print inventory information; for each key print key, price and stock:
for key in prices:
    print(key)
    print ("price: %s" % prices[key])
    print ("stock: %s" % stock[key])

# something of value; total value of inventory:
total = 0
for key in prices:
    item_total = prices[key]*stock[key]
    print(key, item_total)
    total += item_total
print(total)

# shopping at the market; consumer interface:
# create list:
groceries = ["banana", "orange", "apple"]

# making a purchase; how much to pay:


def compute_bill(food):
    total = 0
    for key in food:
        total += prices[key]
    return total
# test:
print(compute_bill(groceries))

# stocking out; take stock/inventory of item when computing cost


def compute_bill(food):
    total = 0
    for key in food:
        if stock[key] > 0:
            total += prices[key]
            stock[key] -= 1
    return total
# test:
print(compute_bill(groceries))

# end of course; covered lists, dictionaries, for loops, functions, updating data in response to the environment

