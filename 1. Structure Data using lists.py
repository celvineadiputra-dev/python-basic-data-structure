nums = [1, 2, 3, 4, 5]
print(nums)

colors = ["Blue", "Purple", "Soft Blue"]
print(colors)

mixed_list = [1, 1.0, 1.1, "Blue", "October", 25]
print(mixed_list)

list_in_list = [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
print(list_in_list)

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list_number)
print(list_number[0])
print(list_number[1])
print(list_number[-1])
print(list_number[5])
print(list_number[0:3])
print(list_number[1:3])
print(list_number[3:])
print(list_number[2:])
print(list_number[2:5])
print(list_number[:5])
print(list_number[-1:])
print(list_number[-4:-1])

print(colors)

print("Blue" in colors)
print("Green" in colors)
print("Green" not in colors)

colors.append("Dark Blue")
print(colors)

colors.insert(3, "Lime Green")
print(colors)

colors.pop()
print(colors)
colors.pop(2)
print(colors)

colors.extend(["Indigo", "Orange"])
print(colors)

del colors[3]
print(colors)

colors[3] = "Gold"
print(colors)

# Output
# [1, 2, 3, 4, 5]
# ['Blue', 'Purple', 'Soft Blue']
# [1, 1.0, 1.1, 'Blue', 'October', 25]
# [[1, 2, 3, 4, 5], [6, 7, 8, 9]]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 1
# 2
# 9
# 6
# [1, 2, 3]
# [2, 3]
# [4, 5, 6, 7, 8, 9]
# [3, 4, 5, 6, 7, 8, 9]
# [3, 4, 5]
# [1, 2, 3, 4, 5]
# [9]
# [6, 7, 8]
# ['Blue', 'Purple', 'Soft Blue']
# True
# False
# True
# ['Blue', 'Purple', 'Soft Blue', 'Dark Blue']
# ['Blue', 'Purple', 'Soft Blue', 'Lime Green', 'Dark Blue']
# ['Blue', 'Purple', 'Soft Blue', 'Lime Green']
# ['Blue', 'Purple', 'Lime Green']
# ['Blue', 'Purple', 'Lime Green', 'Indigo', 'Orange']
# ['Blue', 'Purple', 'Lime Green', 'Orange']
# ['Blue', 'Purple', 'Lime Green', 'Gold']
