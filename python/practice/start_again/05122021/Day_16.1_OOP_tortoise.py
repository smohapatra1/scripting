from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Square", "Charmelon"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align= 'c'
print (table)

