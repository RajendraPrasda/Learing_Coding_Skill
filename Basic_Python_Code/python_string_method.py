# capitalize() method returns a string where the first character is upper case, and the rest is lower case.
txt = "python is FUN!"
x = txt.capitalize()
print(x)

# The casefold() method returns a string where all the characters are lower case.
txt_1 = "Hello, And Welcome To My World!"
x_1 = txt_1.casefold()
print(x_1)

# The center() method will center align the string, using a specified character (space is default) as the fill character.
txt_2 = "banana"
x_2 = txt_2.center(20, "O")
print(x_2)

# The count() method returns the number of times a specified value appears in the string.
txt_3 = "I love apples, apple are my favorite fruit"
x_3 = txt_3.count("apple")
print(x_3)

# The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.
txt_4 = "My name is Ståle"
x_4 = txt_4.encode()
print(x_4)

# Formats specified values in a string
txt_5 = "For only {price:.2f} dollars!"
print(txt_5.format(price=49))

# Searches the string for a specified value and returns the position of where it was found
txt_6 = "Hello, welcome to my world."
x_6 = txt_6.index("welcome")
print(x_6)

myTuple = ("John", "Peter", "Vicky")
x_7 = "#".join(myTuple)
print(x_7)
