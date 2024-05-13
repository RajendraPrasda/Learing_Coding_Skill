# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)
# ===============================
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# ===============================
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


# ===============================
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
