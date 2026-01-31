a, b = 10, 15

try:
    print( a + b )

except TypeError as e: 
    print('Please enter a number in the form of an integer or float!')

except Exception as e:
    print('Something else went wrong....')


print('Continuing with the program...')


