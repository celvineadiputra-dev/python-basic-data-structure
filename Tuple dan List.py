import timeit

# Perbedaan List dan Tuple

# 1. Cara penulisan list dan tuple
# ex : List
nums = list([1, 2, 3, 4, 5])
print(type(nums))
# atau
nums = [1, 2, 3, 4, 5]
print(type(nums))
# ex : Tuple
nums = tuple((1, 2, 3, 4, 5))
print(type(nums))
# atau
nums = (1, 2, 3, 4, 5)
print(type(nums))
# atau
nums = 1, 2, 3, 4, 5
print(type(nums))

print("------------------------------------------------------")

# 2. List bersifat mutable dan tuple immutable
# note : mutable -> Nilai dapat diubah
#        immutable -> Nilai tidak dapat diubah
# ex : List
listNumber = [1, 2, 3, 4, 5]
print(listNumber)

listNumber.pop()
print(listNumber)
# ex : Tuple
tupleNumber = 1, 2, 3, 4, 5
print(tupleNumber)

# tupleNumber.pop()
# print(tupleNumber)
# err : AttributeError: 'tuple' object has no attribute 'pop'

# 3 Tuple menggunakan memori lebih kecil dibanding dengan list
# ex :
listNumber = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tupleNumber = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

print(listNumber.__sizeof__())  # 136
print(tupleNumber.__sizeof__())  # 104

# 4 Waktu membuat object tuple lebih cepat dibanding dengan list
number = 10000
listTime = timeit.repeat(stmt="[1,2,3,4,5,6,7,8,9,10]", number=number, repeat=10)
print(listTime)
tupleNumber = timeit.repeat(stmt="(1,2,3,4,5,6,7,8,9,10)", number=number, repeat=10)
print(tupleNumber)
