count = 0
while count < 10:
    # count will continue up until count
    print("Hello, I am a while and count is", count)
    count += 1


loop_condition = True
while loop_condition:
    # condition decides if the loop will be executed
    # check to see if the loop condition is still true, it not, loop is not executed.
    print("I am a loop")
    loop_condition = False


num = 1
while num < 11:
    # inside loop print value of num squared, increment num
    print(num ** 2)
    num += 1


active = True
choice = input('Enjoying the course? (y/n)')
while True:
    # check input to see if valid; re-prompt
    if choice != 'y' and choice != 'n':
        choice = input("Sorry, I didn't catch that. Enter again: ")
    else:
        break


count = 0
while count < 10:
    # edit to stop infinite loop*
    print(count)
    count = count + 1


count = 0
while True:
    # example of a break
    print(count)
    count += 1
    if count >= 10:
        break


import random
print("Lucky Numbers! 3 numbers will be generated.")
print("If one of them is a '5', you lose!")
count = 0
while count < 3:
    # example of while / else;
    num = random.randint(1, 6)
    print(num)
    if num == 5:
        print("Sorry, you lose!")
        break
    count += 1
else:
    print("You win!")


from random import randint
random_number = randint(1, 10)
guesses_left = 3
while guesses_left > 0:
    # use a while loop - guess number three times
    guess = int(input("Take a guess!: "))
    if guess == random_number:
        print("You win!")
        break
    guesses_left = guesses_left -1
else:
    print("You lose.")


print("Counting...")
# for loop example, count stops before range
for i in range(20):
    print(i)


hobbies = []
for answer in range(3):
    # for loop and append ** answer is key; cannot be hobby
    hobby = input("What is your hobby?: ")
    hobbies.append(hobby)


word = "eggs!"
# Print each letter one at a time
for l in word:
    # l is variable referring to letters in string
    print(l)


phrase = "A bird in the hand..."
# Add your for loop to manipulate, change 'a' with 'X'
for char in phrase:
    if char == 'A' or char == 'a':
        print('X',)
    else:
        print(char,)
# print statement
print()


numbers  = [7, 9, 12, 54, 99]
print("This list contains: ")
for num in numbers:
    # print numbers in list squared on own lines
    print(num**2)


d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
    # print key_space_value associated with key
    print(key, d[key])


choices = ['pizza', 'pasta', 'salad', 'nachos']
print('Your choices are:')
for index, item in enumerate(choices):
    # enumerate works by supplying a corresponding index to each element in the list that you pass it.
    # Each time you go through the loop, index will be one greater, and item will be the next item in the sequence
    print(index +1, item)


list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
for a, b in zip(list_a, list_b):
    # zip creates pairs of elements when passed through two lists
    # print the larger of the two paired elements:
    if a > b:
        print(a)
    else:
        print(b)


fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print('You have...')
for f in fruits:
    # for / else: else only executed if for ends normally (does not end in break)
    if f == 'tomato':
        print('A tomato is not a fruit!') # (It actually is.)
        break # will end in break if tomato is in list
    print('A', f)
else:
    print('A fine selection of fruits!') # will end here if no tomato in list


# new section; CHALLENGE:

def is_even(x):
    # define function to see if num is even
    if abs(x) % 2 == 0: # abs() takes value of number, not the -+
        # % = modulo finds the remainder after division
        return True
    else:
        return False


def is_int(x):
    # integer is a number without a decimal part
    # determine if x is an integer
    if x == int(x):
        return True
    else:
        return False







