nums = [1, 2, 3, 4, 5]
print("data type : {}".format(type(nums)))
print("nums list : {}".format(nums))
print("----------------------------------------")

colors = ["Blue", "Purple", "Soft Blue"]
print("list colors : {}".format(colors))
print("----------------------------------------")

mixed_list = [1, 1.0, 1.1, "Blue", "October", 25]
print("mixed list : {}".format(mixed_list))
print("----------------------------------------")

list_in_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
print("list in list : {}".format(list_in_list))
print("----------------------------------------")

list_number = [1, 3, 4, 5, 1, 3, 9, 2]
print(list_number)
print("length of list_number : {}".format(len(list_number)))
print("min value : {}".format(min(list_number)))
print("max value : {}".format(max(list_number)))
print("count number 1 in list : {}".format(list_number.count(1)))
list_number.reverse()
print("Result of reverse list : {}".format(list_number))
list_number.sort()
print("Sort list : {}".format(list_number))
print("----------------------------------------")

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10]
print(list_number)
print("Index 0 : {}".format(list_number[0]))
print("Index 1 : {}".format(list_number[1]))
print("Last index : {}".format(list_number[-1]))
print("Index 5 : {}".format(list_number[5]))
print("Get position 0 to 3 : {}".format(list_number[0:3]))
print("Get position 1 to 3 : {}".format(list_number[1:3]))
print("Get Position start 3 : {}".format(list_number[3:]))
print("Get Position start 2 : {}".format(list_number[2:]))
print("Get position 2 to 5 : {}".format(list_number[2:5]))
print("Get position until 5 : {}".format(list_number[:5]))
print("Get position -1 : {}".format(list_number[-1:]))
print("Get position -4 to -1 : {}".format(list_number[-4:-1]))
print("Index start form 0")
print("----------------------------------------")

print(colors)

print("Blue in list colors ? {}".format("Blue" in colors))
print("Green in list of colors ? {}".format("Green" in colors))
print("Green not in list of colors ? {}".format("Green" not in colors))

colors.append("Dark Blue")
print("Add dark blue in last list : {}".format(colors))

colors.insert(3, "Lime Green")
print("Insert lime green in index 3 : {}".format(colors))

colors.pop()
print("pop list colors : {}".format(colors))
colors.pop(2)
print("pop index 2 in colors : {}".format(colors))

colors.extend(["Indigo", "Orange"])
print("Add Indigo and Orange colors to colors list : {}".format(colors))

del colors[3]
print("Remove color in list of color with index 3 : {}".format(colors))

colors[3] = "Gold"
print("Change color with index 3 in list of colors : {}".format(colors))
print("----------------------------------------")

# Output
# data type : <class 'list'>
# nums list : [1, 2, 3, 4, 5]
# ----------------------------------------
# list colors : ['Blue', 'Purple', 'Soft Blue']
# ----------------------------------------
# mixed list : [1, 1.0, 1.1, 'Blue', 'October', 25]
# ----------------------------------------
# list in list : [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
# ----------------------------------------
# [1, 3, 4, 5, 1, 3, 9, 2]
# length of list_number : 8
# min value : 1
# max value : 9
# count number 1 in list : 2
# Result of reverse list : [2, 9, 3, 1, 5, 4, 3, 1]
# Sort list : [1, 1, 2, 3, 3, 4, 5, 9]
# ----------------------------------------
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 10]
# Index 0 : 1
# Index 1 : 2
# Last index : 10
# Index 5 : 6
# Get position 0 to 3 : [1, 2, 3]
# Get position 1 to 3 : [2, 3]
# Get Position start 3 : [4, 5, 6, 7, 8, 9, 1, 10]
# Get Position start 2 : [3, 4, 5, 6, 7, 8, 9, 1, 10]
# Get position 2 to 5 : [3, 4, 5]
# Get position until 5 : [1, 2, 3, 4, 5]
# Get position -1 : [10]
# Get position -4 to -1 : [8, 9, 1]
# Index start form 0
# ----------------------------------------
# ['Blue', 'Purple', 'Soft Blue']
# Blue in list colors ? True
# Green in list of colors ? False
# Green not in list of colors ? True
# Add dark blue in last list : ['Blue', 'Purple', 'Soft Blue', 'Dark Blue']
# Insert lime green in index 3 : ['Blue', 'Purple', 'Soft Blue', 'Lime Green', 'Dark Blue']
# pop list colors : ['Blue', 'Purple', 'Soft Blue', 'Lime Green']
# pop index 2 in colors : ['Blue', 'Purple', 'Lime Green']
# Add Indigo and Orange colors to colors list : ['Blue', 'Purple', 'Lime Green', 'Indigo', 'Orange']
# Remove color in list of color with index 3 : ['Blue', 'Purple', 'Lime Green', 'Orange']
# Change color with index 3 in list of colors : ['Blue', 'Purple', 'Lime Green', 'Gold']
