# File Handling in Python.

# Reading a file.
with open('my_file.txt', mode='r') as file:
    content = file.read()
    print(content)

# Writing some content to a file.
content = '\nMy favourite show is Peppa Pig.'
with open('new_file.txt', mode='w') as file:
    file.write(content)


# Adding some content to an exiting file.
with open('my_file.txt', mode='a') as file:
    file.write(content)