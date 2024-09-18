# Any message after a '#' will be commented out and will not be run.

# === Types ===
# There are 4 main data types: str, int, bool, float
# type annotations are useful but optional
name: str = "Bob"
age: int = 20
alive: bool = True
money: float = 3.45

# === Basic Output ===
# We can print out some text to the console
print("Hello World!")  # Hello World!
print("Anything", "at", "All")  # Anything at All
# We can also do arithmatic
print(1 + 2)  # 3
print(3 - 4.5)  # -1.5
print(5 * 6)  # 30
# We can also print the variables
print(name)  # Bob
print(age)  # 20
print(alive)  # True
print(money)  # 3.45

# === Variables ===
# As before, we can store values in variable
a = 10
print(a)  # 10
# We can also override them
a = 20
print(a)  # 20
# or change them
a = a + 10
print(a)  # 30
# or use them in other variables
b = a - 5
print(b)  # 25
# We can even make multiple variables in one line of
c = d = 3
print(c, d)
# or different values
e, f = "Hello", "Goodbye"
print(e, f)
