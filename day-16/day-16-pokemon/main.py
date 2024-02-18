from prettytable import PrettyTable

table = PrettyTable()

# # Adding columns
# table.add_column("Characters", ["Pikachu", "Vivillon", "Simipour", "Scolipede"])
# table.add_column("Type", ["Electric", "Flying", "Water", "Poison"])

# Adding rows.
table.field_names = ["Pokemon Name", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Vivillon", "Flying"])
# table.add_row(["Simipour", "Water"])
# table.add_row(["Scolipede", "Poison"])

data = [
   ["Pikachu", "Electric"],
   ["Vivillon", "Flying"],
   ["Simipour", "Water"],
   ["Scolipede", "Poison"],
]

# Add rows together.
table.add_rows(data)

# Change data alignment.
table.align = 'l'

print(table)