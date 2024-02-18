# List Comprehension.
# Syntax: new_list = [new_item for item in list]
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = 'Debaditya'
letters = [letter for letter in name]
print(letters)

double_number = [n * 2 for n in range(1,5)]
print(double_number)

# Conditional List Comprehension.
# Syntax: new_list = [new_item for item in list if test]
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names_cap = [name.upper() for name in names if len(name) > 4]
print(long_names_cap)

# Dictionary Comprehension.
# Syntax: new_dict = {new_key:new_value for item in list}
# Syntax: new_dict = {new_key:new_value for (key, value) in dict.items()}
from random import randint
student_score = {student:randint(30, 100) for student in names}
print(student_score)

# Conditional Dictionary Comprehension.
# Syntax: new_dict = {new_key:new_value for (key, value) in dict.items() if test}
passed_students = {student:score for (student, score) in student_score.items() if score >= 60}
print(passed_students)