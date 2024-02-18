# # 1. Using simple file handling.
# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()

# print(data)

# # 2. Importing 'csv' module.
# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)

#     temparature = []

#     for row in data:
#         if row[1] != 'temp':
#             temparature.append(int(row[1]))
        
#     print(temparature)

# 3. Importing 'pandas' module.
import pandas 

data = pandas.read_csv('weather_data.csv')

# Get a column in the dataframe.
print('\nGet a column in the dataframe')
print(data['condition'])
# print(data.condition)

# Get a row in the dataframe [using a where condition].
print('\nGet a row in the dataframe')
print(data[data['day'] == 'Monday'])

# Calculating average temperature.
# temp_list = data['temp'].to_list()
# avg_temp = round(sum(temp_list) / len(temp_list), 2) 
avg_temp = round(data['temp'].mean(), 2) 
print(f'\nAverage Temparature: {avg_temp} degree celcius.')

# Calculating Max temparature.
print(f'Max. Temperature: {data['temp'].max()} degree celcius.')

# Get the row of data which have highest temparature of the week.
print('\nGet the row of data which have highest temparature of the week.')
print(data[data['temp'] == data['temp'].max()])

# Convert monday's temprature into Fahrenheit.
monday = data[data.day == 'Monday']
monday_temp_fahrenheit = (monday.temp[0] * 1.8) + 32
print(f'\nThe temperature of monday into degree F: {monday_temp_fahrenheit}')

# Creating dataframe from scratch. [from python dictionary]
student_data = {
    'students': ['Anurag', 'Sofie', 'Rahul', 'Amy'],
    'scores': [98, 86, 76, 69]
}

data = pandas.DataFrame(student_data)
# print(data)
# Save the data into csv file.
data.to_csv('student_score.csv')


