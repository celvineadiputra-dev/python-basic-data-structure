# Set (Immutable)

set_nums = set((1, 1, 8, 2, 3, 4, 5, 6))
set_nums2 = {8, 1, 1, 2, 3, 4, 5, 6}

print(type(set_nums))
print(type(set_nums2))

# tidak bisa memiliki value yang duplicate
# value akan selalu berurutan
print(set_nums)
print(set_nums2)

print(set("Debb"))

# Output
# <class 'set'>
# <class 'set'>
# {1, 2, 3, 4, 5, 6, 8}
# {1, 2, 3, 4, 5, 6, 8}
# {'D', 'b', 'e'}
