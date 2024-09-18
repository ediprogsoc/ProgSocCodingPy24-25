# === Arithmatic ===
# Addition
print(1 + 2)  # 3
# Subtraction
print(3 - 2)  # 1
# Multiplication and Powers
print(4 * 5)  # 20
print(6 ** 2)  # 36
# Note that it is ** and not ^. ^ is used for boolean XOR
# Division and Modulo
print(6 / 2)  # 3.0
print(5 / 2)  # 2.5
print(5 // 2)  # 2
# Note that a single / is float division whilst double / (//) is integer division and will round down
print(7 % 3)  # 1
# % means to take the remainder after dividing

# === Strings ===
name: str = "John"
# We can add to a string
print(name + "ny")  # Johnny
# We can use string methods to change the string
print(name.lower())  # john
print(name.upper())  # JOHN
print(name.swapcase())  # jOHN
print(name.split("o"))  # [J, hn]
# or we can use it to find out information about the string
print(name.find("h"))  # 2
print(name.index("h"))  # 2
print(name.count("o"))  # 1
print(name.isascii())  # True
print(name.isdigit())  # False
# We can also index a string with square brackets
# Indexing starts and 0
print(name[0])  # J
print(name[1:])  # ohn
print(name[2:-1])  # h
print(name[::2])  # Jh

# === Booleans ===
# Booleans (bool) can be either True or False
# Any comparison will produce a bool
a, b = 2, 6
print(a == b)  # False
print(a >= b)  # False
print(a < b)  # True
# It also works with strings
print("Good" in "Goodbye")  # True
