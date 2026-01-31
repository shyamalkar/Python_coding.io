text = 'aplle' # String

numbers = 10 # int

decimal = -10.123 # float , float can be negative and positive both accept.

has_money = True # boolean , boolean True & False both are accept 

coordinates = (2.5, 1.5, 1.0) # Decimal

names = ['Agnetha', 'bjorn', 'Benny', 'Anni-frid'] # list
 # i crate a list for square and bracket , which means i can remove element's and add element's

unique = {1, 2, 3, 4, 4, 5} # a set , recently i called this unique because a set never repeat again. i can write duplicate but if i print this this duplicate are dissipare.

users = {'Bob': 1, 'james': 2} # dictionary


print(numbers, decimal, has_money, coordinates, names, unique, users)


# Some time we want to convert a data type string to integer.

number = '100'
print(float('123.456')) 

age: int = 10
name: str = 'Bob'

print('Name: ' + name + ', Age: ' + str(age))
print(f"Name: {name}, Age:{age}")

# Now we gonna create a function
def add(a: float, b: float) -> float:
    print(f'Adding: {a} + {b}')
    return a + b 

print(add(10, + 15))
print(add(15, + 30))