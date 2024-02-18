# This program analyze the 2018 Squirrel Census data from NYC Central Park and create an output file
# containing the counts of different squirrels of different fur color.

import pandas as pd

squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# Get the list of available fur colors.
fur_colors = squirrel_data['Primary Fur Color'].dropna().unique().tolist()
# print(fur_colors)

# Get the counts of squirrels of different fur colors.
counts = []
for color in fur_colors:
    counts.append(squirrel_data[squirrel_data['Primary Fur Color'] == color].shape[0]) 

# Create a dictionary of the counts of different squirrels of different fur color.
squirrel_dict = {
    'SquirrelFurColor': fur_colors,
    'SquirrelCounts': counts
}

# Create the dataframe and save it to output file.
squirrel_color_stats = pd.DataFrame(squirrel_dict)
squirrel_color_stats.to_csv('Squirrel_Color_Statistics.csv')
    