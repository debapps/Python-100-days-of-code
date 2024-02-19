# This program deals with runtime errors/exceptions.
# Rutime error = Exception.

# TypeError
# a = 'Hello'
# print(a + 5)

# IndexError.
# citys = ['Kolkata', 'Delhi', 'Mumbai', 'Chennai']
# print(citys[4])

# ZeroDivisionError
# print(3.14 / 0)

# FileNotFoundError
# with open('Hello.txt') as file:
#     content = file.read() 

# KeyError
# book_dict = {'The Three Musketeers': 'Alexandre Dumas',
#              'Romeo and Juliet': 'William Shakespeare',
#              'A Study in Scarlet': 'Arthur Conan Doyle'}
# print(book_dict['The Sign of the Four'])

# The following four keywords are used to handle execeptions.
# try: This block holds the code that might cause an exception.
# except: This block holds the code that will be executed when there is an exception.
# else: This block holds the code that will be executed when there is no exception.
# finally: This block holds the code that will be executed no matter what happens.

try:
    file = open('hello.txt')
    book_dict = {'The Three Musketeers': 'Alexandre Dumas',
             'Romeo and Juliet': 'William Shakespeare',
             'A Study in Scarlet': 'Arthur Conan Doyle'}
    print(book_dict['A Study in Scarlet'])
    # print(book_dict['The Sign of the Four'])
except FileNotFoundError:
    file = open('hello.txt', 'w')
    file.write('Hello, World!')
except KeyError as err:
    print(f'ERROR: The key - {err} does not exist!')
else:
    data = file.read()
    print(data)
finally:
    print('The file is closed now.')
    file.close()

# Raising user exceptions.
print('\nBMI Calculation\n')
height = float(input('Height: '))
weight = int(input('Weight: '))

if height > 3:
    raise ValueError('Human height can not be greater than 3 meters.')

bmi = weight / height ** 2
print(f'\nBMI - {bmi}')