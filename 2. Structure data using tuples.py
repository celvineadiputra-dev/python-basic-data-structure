# Tuple (Immutable)

nums = tuple((1, 2, 3, 4, 5))
nums1 = (1, 2, 3, 4, 5)
nums2 = 1, 2, 3, 4, 5
print("data type : {}".format(type(nums)))
print("data type : {}".format(type(nums1)))
print("data type : {}".format(type(nums2)))
print("nums list : {}".format(nums))
print("----------------------------------------")

colors = ("Blue", "Purple", "Soft Blue")
print("list colors : {}".format(colors))
print("----------------------------------------")

mixed_list = (1, 1.0, 1.1, "Blue", "October", 25)
print("mixed list : {}".format(mixed_list))
print("----------------------------------------")

list_in_list = ((1, 2, 3, 4, 5), (6, 7, 8, 9))
print("list in list : {}".format(list_in_list))
print("----------------------------------------")

tuple_number = (1, 3, 4, 5, 1, 3, 9, 2)
print(tuple_number)
print("length of tuple_number : {}".format(len(tuple_number)))
print("min value : {}".format(min(tuple_number)))
print("max value : {}".format(max(tuple_number)))
print("count number 1 in list : {}".format(tuple_number.count(1)))
print("Tuple tidak bisa di reverse dengan .reverse()")
print("Tuple tidak bisa di sort dengan .sort()")
print("----------------------------------------")

tuple_number = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10)
print(tuple_number)
print("Index 0 : {}".format(tuple_number[0]))
print("Index 1 : {}".format(tuple_number[1]))
print("Last index : {}".format(tuple_number[-1]))
print("Index 5 : {}".format(tuple_number[5]))
print("Get position 0 to 3 : {}".format(tuple_number[0:3]))
print("Get position 1 to 3 : {}".format(tuple_number[1:3]))
print("Get Position start 3 : {}".format(tuple_number[3:]))
print("Get Position start 2 : {}".format(tuple_number[2:]))
print("Get position 2 to 5 : {}".format(tuple_number[2:5]))
print("Get position until 5 : {}".format(tuple_number[:5]))
print("Get position -1 : {}".format(tuple_number[-1:]))
print("Get position -4 to -1 : {}".format(tuple_number[-4:-1]))
print("Index start form 0")
print("----------------------------------------")

print(colors)

print("Blue in list colors ? {}".format("Blue" in colors))
print("Green in list of colors ? {}".format("Green" in colors))
print("Green not in list of colors ? {}".format("Green" not in colors))

print("Tuple bersifat immutable (tidak bisa di ubah)")
print("----------------------------------------")

# Output
# data type : <class 'tuple'>
# data type : <class 'tuple'>
# data type : <class 'tuple'>
# nums list : (1, 2, 3, 4, 5)
# ----------------------------------------
# list colors : ('Blue', 'Purple', 'Soft Blue')
# ----------------------------------------
# mixed list : (1, 1.0, 1.1, 'Blue', 'October', 25)
# ----------------------------------------
# list in list : ((1, 2, 3, 4, 5), (6, 7, 8, 9))
# ----------------------------------------
# (1, 3, 4, 5, 1, 3, 9, 2)
# length of tuple_number : 8
# min value : 1
# max value : 9
# count number 1 in list : 2
# Tuple tidak bisa di reverse dengan .reverse()
# Tuple tidak bisa di sort dengan .sort()
# ----------------------------------------
# (1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10)
# Index 0 : 1
# Index 1 : 2
# Last index : 10
# Index 5 : 6
# Get position 0 to 3 : (1, 2, 3)
# Get position 1 to 3 : (2, 3)
# Get Position start 3 : (4, 5, 6, 7, 8, 9, 1, 10)
# Get Position start 2 : (3, 4, 5, 6, 7, 8, 9, 1, 10)
# Get position 2 to 5 : (3, 4, 5)
# Get position until 5 : (1, 2, 3, 4, 5)
# Get position -1 : (10,)
# Get position -4 to -1 : (8, 9, 1)
# Index start form 0
# ----------------------------------------
# ('Blue', 'Purple', 'Soft Blue')
# Blue in list colors ? True
# Green in list of colors ? False
# Green not in list of colors ? True
# Tuple bersifat immutable (tidak bisa di ubah)
# ----------------------------------------
