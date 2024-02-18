# Unlimited Positional Arguments.
# This function adds unlimited numbers passed as arguments.
def add(*args):
    # 'args' is a tuple.
    # print(args)
    sum = 0

    for n in args:
        sum += n

    return sum

# Unlimited Keyword Arguments.
# This function accepts multiple/unlimited keyword arguments.
def calculate(n, **kwargs):
    # 'kwargs is a dictionary'

    keys = kwargs.keys()

    if 'multiply' in keys:
        n *= kwargs['multiply']

    if 'devide' in keys:
        n /= kwargs['devide'] 

    if 'plus' in keys:
        n += kwargs['plus']
    
    if 'minus' in keys:
         n -= kwargs['minus']

    return n


result = calculate(2, multiply=4, minus=-8)
result = add(1,3,4,6)
# print(result)

# Initializing class using unlimited keyword arguments.

class Car:

    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.year = kw.get('year')
        self.color = kw.get('color')

    def display(self):
        print(f' Make: {self.make}\n Model: {self.model}\n Year: {self.year}\n Color: {self.color}\n')
    
car1 = Car(make='Toyota', model='Camry LE', year=2012, color='White')
car1.display()

car2 = Car(make='Dodge', model='Charger', year=2023)
car2.display()
