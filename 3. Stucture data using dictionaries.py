# Dictionary (Mutable)

dataExampleFavoriteColor = {
    'Jhon': 'Blue',
    'Taris': 'Soft Blue',
    'Debb': 'Sky Blue'
}

dataExampleFavoriteColor2 = dict({
    'Jhon': 'Blue',
    'Taris': 'Soft Blue',
    'Debb': 'Sky Blue'
})

print("Data type : {}".format(type(dataExampleFavoriteColor)))
print("Data type : {}".format(type(dataExampleFavoriteColor2)))
print(dataExampleFavoriteColor)
print(dataExampleFavoriteColor2)

print(dataExampleFavoriteColor['Debb'])
print(dataExampleFavoriteColor['Taris'])

dataExampleFavoriteColor['Jhon'] = "Dark Blue"
print(dataExampleFavoriteColor)

del dataExampleFavoriteColor['Jhon']
print(dataExampleFavoriteColor)

dataExampleFavoriteColor['Doe'] = "Red"
print(dataExampleFavoriteColor)

# Output
# Data type : <class 'dict'>
# Data type : <class 'dict'>
# {'Jhon': 'Blue', 'Taris': 'Soft Blue', 'Debb': 'Sky Blue'}
# {'Jhon': 'Blue', 'Taris': 'Soft Blue', 'Debb': 'Sky Blue'}
# Sky Blue
# Soft Blue
# {'Jhon': 'Dark Blue', 'Taris': 'Soft Blue', 'Debb': 'Sky Blue'}
# {'Taris': 'Soft Blue', 'Debb': 'Sky Blue'}
# {'Taris': 'Soft Blue', 'Debb': 'Sky Blue', 'Doe': 'Red'}
