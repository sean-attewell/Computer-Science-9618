# Multiplies, then divides, then adds

my_number = 2 + 2 * 8 / 5.0
print(my_number)  

# the argument for the print function can be an expression. 
# Once the expression is resolved to a string object, the print function can output it to the screen.

print(2 + 2 * 8 / 5.0)

# There is also an operator called the modulo operator (%). This operator returns the remainder of integer division.

my_remainder = 9 % 4
print(my_remainder)  # 1


# Floor Division is like the inverse of this. Dividing with two // means you instead don't get any remainder
# You are just left with the quotient in which the digits after the decimal point are removed. 
no_remainder = 9 // 4
print(no_remainder)  # 2

# But if one of the operands is negative, the result is still floored, i.e. still rounded down (towards negative infinity).
# So -11/3 = -3.666 so it rounds it toward negative infinity and you get -4

# You can use two multiplication operators to make the exponentiation operator (**).
two_squared = 2 ** 2
print(two_squared)    # 4
two_cubed = 2 ** 3
print(two_cubed)      # 8

# You can use the operators on variable names directly
print(two_cubed - two_squared)

# You can use the addition operator to concatenate strings and lists:
string_one = "Hello,"
string_two = " World!"
combined = string_one + string_two
print(combined)  # Hello, World!

lst_one = [1, 2, 3]
lst_two = [4, 5, 6]
big_lst = lst_one + lst_two
print(big_lst)  # [1, 2, 3, 4, 5, 6]

# You can also use the multiplication operator to create a new list or string that repeats the original sequence:

my_string = "Bueller"
repeated = my_string * 3
print(repeated)  # BuellerBuellerBueller

my_list = [1, 2, 3]
repeated_list = my_list * 3
print(repeated_list)  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# The add and multiply operators working on multiple different types (integers and strings) is a kind of polymorphism: 
# the provision of a single interface to entities of different types