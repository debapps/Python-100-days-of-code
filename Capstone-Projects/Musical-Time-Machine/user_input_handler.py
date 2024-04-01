from datetime import datetime

# This module handles and validates the user input.

class UserInputHandler:

    def __init__(self) -> None:
        self.valid_date = None

    def format_valid_date(self, input_date):
        try:
            format_date = datetime.strptime(input_date, '%Y-%m-%d')
            
            if format_date.month < 10:
                month = f'0{format_date.month}'
            else:
                month = str(format_date.month)

            if format_date.day < 10:
                day = f'0{format_date.day}'
            else:
                day = str(format_date.day)

            self.valid_date = f'{str(format_date.year)}-{month}-{day}'
        except ValueError:
            print('Invalid Date!')
        


    def get_user_date(self): 
        while self.valid_date == None:
            # Get the date from the user.
            date = input('Which year do you want to travel to? Type a date in the format YYYY-MM-DD:\n')
            self.format_valid_date(date)

        return self.valid_date