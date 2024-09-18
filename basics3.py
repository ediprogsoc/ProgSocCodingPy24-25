# === Tuples ===
a: tuple[int] = (1, 2, 3)
print(a)  # (1, 2, 3)
print(a[0])  # 1
print(a[1:])  # (2, 3)
# Tuples are a fixed length, and you cannot change the contents
# === Lists ===
# On the other hand, lists can change.
b: list[int] = [4, 5, 6]
print(b)  # [4, 5, 6]
b.append(7)  # Adds a value to the end of a list
print(b)  # [4, 5, 6, 7]
b.remove(5)  # Removes a value
print(b)  # [4, 6, 7]
b.insert(2, 9)  # Index, then the value
print(b)  # [4, 6, 9, 7]
b.extend([8, 9, 10])  # Adds a list to the end
print(b)  # [4, 6, 9, 7, 8, 9, 10]
b.sort()  # Sorts the list
print(b)  # [4, 6, 7, 8, 9, 9, 10]
c = b.pop(1)  # Returns a value at an index
print(c)  # 6
print(b)  # [4, 7, 8, 9, 9, 10]
b.reverse()
print(b)  # [10, 9, 9, 8, 7, 4]
b.clear()  # Empties the list
print(b)  # []

# === Sets ===
# A set is similar to a list but cannot contain duplicates and has no order
d = {1, 2, 3}
print(d)  # {1, 2, 3}
d.add(4)
print(d)  # {1, 2, 3, 4}
d.add(4)
print(d)  # {1, 2, 3, 4}
d.remove(1)
print(d)  # {2, 3, 4}
# You can use sets the same way you do with mathematical sets
print(d.intersection({3, 4, 5}))  # {3, 4}
print(d.union({3, 4, 5}))  # {2, 3, 4, 5}
d.clear()
print(d)  # set()

# === Dictionaries ===
# A dictionary (dict) is python's Hashmap
e = {1: "a", 2: "b", 3: "c"}
# A dict is a set of key-value pairs
print(e)  # {1: "a", 2: "b", 3: "c"}
# You can only index at a key
print(e[1])  # a
# You can also get information from dicts
print(e.keys())  # dict_keys([1, 2, 3])
print(e.values())  # dict_values(['a', 'b', 'c'])
print(e.items())  # dict_items([(1, 'a'), (2, 'b'), (3, 'c')])
print(e.pop(2))  # b
print(e)  # {1: 'a', 3: 'c'}
