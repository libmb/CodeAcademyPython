
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
