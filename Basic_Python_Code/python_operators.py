# Operators are used to perform operations on variables and values.
# Arithmetic operators
# Assignment operators
# Comparison operators
# Logical operators
# Identity operators
# Membership operators
# Bitwise operators

# Arithmetic operators
a = 200
b = 20
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a % b)
print(a**b)
print(a//b)

# Comparison operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x >= y)
print(x <= y)

# Logical operators
c = 5
print(c > 3 and c < 10)
print(c > 3 or c < 10)
print(not(x < 5 and x < 10))

# Identity operators
d = ["apple", "banana"]
e = ["apple", "banana"]
f = d

print(d is f)
# returns True because z is the same object as x
print(d is e)
# returns False because x is not the same object as y, even if they have the same content
print(d == e)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

# Membership operators
n = ["apple", "banana"]
print("banana" in n)

m = ["apple", "banana"]
print("pineapple" not in m)
